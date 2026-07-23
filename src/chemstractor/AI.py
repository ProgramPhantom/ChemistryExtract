import os
import json
from typing import Literal, get_args, Union
from dotenv import load_dotenv
from google import genai
from google.genai import types
import ollama
from pydantic import BaseModel

load_dotenv()

pricing_matrix = {
    "gemini-2.5-flash": {
        "input_per_m": 0.30,   # $0.30 per 1M tokens
        "output_per_m": 2.50    # $2.50 per 1M tokens
    },
    "gemini-2.5-pro": {
        "input_per_m": 1.25,    # $1.25 per 1M tokens
        "output_per_m": 10.00   # $10.00 per 1M tokens
    },
    "gemini-3.5-flash": {
        "input_per_m": 1.50,    # $1.50 per 1M tokens
        "output_per_m": 9.00    # $9.00 per 1M tokens
    },
    "gemini-3.1-flash-lite": {
        "input_per_m": 0.25,    # $0.25 per 1M tokens
        "output_per_m": 1.50    # $1.50 per 1M tokens
    }
}

OnlineModels = Literal["gemini-2.5-flash", "gemini-2.5-pro", "gemini-3.5-flash"]
OfflineModels = Literal["qwen3.6:35b", "gemma4:31b"]
AllSupportedModels = Union[OnlineModels, OfflineModels]

ONLINE_MODELS = list(pricing_matrix.keys())
OFFLINE_MODELS = list(get_args(OfflineModels))


class AIPromptResult:
    """Standardized response from prompt calls, containing success status, parsed data, and token usage."""
    def __init__(self, success: bool, error: str = "", data: BaseModel = None, usage_metadata: dict = None, calculator_calls: list = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata
        self.calculator_calls = calculator_calls or []


class AI:
    pricing_matrix = pricing_matrix
    ONLINE_MODELS = ONLINE_MODELS
    OFFLINE_MODELS = OFFLINE_MODELS
    DEFAULT_MODEL = "gemma4:31b"
    
    _instance = None
    
    @classmethod
    def get_instance(cls) -> 'AI':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self, default_model: AllSupportedModels = DEFAULT_MODEL):
        self.selected_model = default_model
        self.total_prompt_tokens = 0
        self.total_candidate_tokens = 0
        self.total_tokens = 0
        
        self.api_key = os.getenv('API_KEY')
        self.client = None
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
            
        AI._instance = self

    def set_selected_model(self, model: AllSupportedModels):
        if model not in self.ONLINE_MODELS and model not in self.OFFLINE_MODELS:
            raise ValueError(f"Unsupported model: {model}")
        self.selected_model = model

    def preload_model(self):
        """Preloads the selected model if it is an offline (local Ollama) model."""
        if self.selected_model in self.OFFLINE_MODELS:
            try:
                ollama.generate(model=self.selected_model, prompt='')
            except Exception as e:
                raise RuntimeError(
                    f"Failed to preload local Ollama model '{self.selected_model}'. "
                    f"Please make sure Ollama is running and the model is pulled. "
                    f"Error: {e}"
                )


    def prompt(self, prompt: str, schema: type[BaseModel], model: AllSupportedModels = None, temperature: float = 0.0, tools: list = None, system_instruction: str = None) -> AIPromptResult:
        """General prompt endpoint which routes requests to either Gemini or local Ollama depending on the model."""
        if model is None:
            model = self.selected_model
            
        if model in self.ONLINE_MODELS:
            return self._prompt_gemini(prompt, schema, model, temperature, tools, system_instruction)
        elif model in self.OFFLINE_MODELS:
            return self._prompt_local(prompt, schema, model, temperature, tools, system_instruction)
        else:
            return AIPromptResult(success=False, error=f"Unsupported model: {model}")

    def _prompt_gemini(self, prompt: str, schema: type[BaseModel], model: str, temperature: float, tools: list = None, system_instruction: str = None) -> AIPromptResult:
        if not self.client:
            self.api_key = os.getenv('API_KEY')
            if self.api_key:
                self.client = genai.Client(api_key=self.api_key)
            else:
                return AIPromptResult(success=False, error="API_KEY environment variable is not set.")
                
        try:
            if not tools:
                config = types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=temperature,
                )
                if system_instruction:
                    config.system_instruction = system_instruction
                    
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=config,
                )
                usage = None
                if hasattr(response, 'usage_metadata') and response.usage_metadata:
                    usage = {
                        "prompt_token_count": response.usage_metadata.prompt_token_count,
                        "candidates_token_count": response.usage_metadata.candidates_token_count,
                        "total_token_count": response.usage_metadata.total_token_count
                    }
                    self.total_prompt_tokens += usage.get("prompt_token_count", 0) or 0
                    self.total_candidate_tokens += usage.get("candidates_token_count", 0) or 0
                    self.total_tokens += usage.get("total_token_count", 0) or 0
                    
                return AIPromptResult(success=True, error="", data=response.parsed, usage_metadata=usage)
                
            # If tools are provided, we run the tool calling loop
            tool_map = {func.__name__: func for func in tools}
            contents = [prompt]
            config = types.GenerateContentConfig(
                tools=tools,
                temperature=temperature,
            )
            if system_instruction:
                config.system_instruction = system_instruction
                
            calculator_calls = []
            max_turns = 10
            
            for turn in range(max_turns):
                response = self.client.models.generate_content(
                    model=model,
                    contents=contents,
                    config=config,
                )
                
                # Check for function/tool calls in the response
                if response.function_calls:
                    contents.append(response.candidates[0].content)
                    
                    tool_responses = []
                    for fc in response.function_calls:
                        func_name = fc.name
                        func = tool_map.get(func_name)
                        if func:
                            args = fc.args
                            expr = args.get('expression') if isinstance(args, dict) else args
                            
                            try:
                                if isinstance(args, dict):
                                    result = func(**args)
                                else:
                                    result = func(args)
                            except Exception as e:
                                result = f"Error: {e}"
                                
                            calculator_calls.append({
                                "expression": expr,
                                "result": result
                            })
                            
                            tool_responses.append(
                                types.Part.from_function_response(
                                    name=func_name,
                                    response={"result": result}
                                )
                            )
                    
                    contents.append(types.Content(role="user", parts=tool_responses))
                else:
                    # No function calls, get the final output using the schema
                    if schema:
                        contents.append("Now, present the final extracted data strictly adhering to the JSON schema.")
                        final_config = types.GenerateContentConfig(
                            response_mime_type="application/json",
                            response_schema=schema,
                            temperature=temperature,
                        )
                        if system_instruction:
                            final_config.system_instruction = system_instruction
                            
                        final_res = self.client.models.generate_content(
                            model=model,
                            contents=contents,
                            config=final_config,
                        )
                        
                        usage = None
                        if hasattr(final_res, 'usage_metadata') and final_res.usage_metadata:
                            usage = {
                                "prompt_token_count": final_res.usage_metadata.prompt_token_count,
                                "candidates_token_count": final_res.usage_metadata.candidates_token_count,
                                "total_token_count": final_res.usage_metadata.total_token_count
                            }
                            self.total_prompt_tokens += usage.get("prompt_token_count", 0) or 0
                            self.total_candidate_tokens += usage.get("candidates_token_count", 0) or 0
                            self.total_tokens += usage.get("total_token_count", 0) or 0
                            
                        return AIPromptResult(success=True, error="", data=final_res.parsed, usage_metadata=usage, calculator_calls=calculator_calls)
                    else:
                        return AIPromptResult(success=True, error="", data=response.text, calculator_calls=calculator_calls)
                        
            return AIPromptResult(success=False, error="Exceeded maximum tool calling turns.", calculator_calls=calculator_calls)
            
        except Exception as e:
            return AIPromptResult(success=False, error=str(e))

    def _prompt_local(self, prompt: str, schema: type[BaseModel], model: str, temperature: float, tools: list = None, system_instruction: str = None) -> AIPromptResult:
        try:
            if not tools:
                messages = []
                if system_instruction:
                    messages.append({'role': 'system', 'content': system_instruction})
                messages.append({'role': 'user', 'content': prompt})
                
                response = ollama.chat(
                    model=model,
                    messages=messages,
                    format=schema.model_json_schema() if schema else None,
                    options={'temperature': temperature}
                )
                raw_json_string = response['message']['content']
                parsed_data = json.loads(raw_json_string)
                data = schema(**parsed_data) if schema else raw_json_string
                
                usage = None
                prompt_tokens = response.get('prompt_eval_count', 0)
                eval_tokens = response.get('eval_count', 0)
                if prompt_tokens or eval_tokens:
                    usage = {
                        "prompt_token_count": prompt_tokens,
                        "candidates_token_count": eval_tokens,
                        "total_token_count": prompt_tokens + eval_tokens
                    }
                    self.total_prompt_tokens += prompt_tokens
                    self.total_candidate_tokens += eval_tokens
                    self.total_tokens += (prompt_tokens + eval_tokens)
                    
                return AIPromptResult(success=True, error="", data=data, usage_metadata=usage)

            # If tools are provided, run tool calling loop
            tool_map = {func.__name__: func for func in tools}
            messages = []
            if system_instruction:
                messages.append({'role': 'system', 'content': system_instruction})
            messages.append({'role': 'user', 'content': prompt})
            
            calculator_calls = []
            max_turns = 10
            
            for turn in range(max_turns):
                response = ollama.chat(
                    model=model,
                    messages=messages,
                    tools=tools,
                    options={'temperature': temperature}
                )
                
                tool_calls = response['message'].get('tool_calls')
                if tool_calls:
                    messages.append(response['message'])
                    
                    for tc in tool_calls:
                        func_name = tc['function']['name']
                        func = tool_map.get(func_name)
                        if func:
                            args = tc['function']['arguments']
                            expr = args.get('expression') if isinstance(args, dict) else args
                            
                            try:
                                if isinstance(args, dict):
                                    result = func(**args)
                                else:
                                    result = func(args)
                            except Exception as e:
                                result = f"Error: {e}"
                                
                            calculator_calls.append({
                                "expression": expr,
                                "result": result
                            })
                            
                            messages.append({
                                'role': 'tool',
                                'content': str(result),
                                'name': func_name
                            })
                else:
                    if schema:
                        try:
                            messages.append({
                                'role': 'user',
                                'content': "Now, present the final extracted data strictly adhering to the JSON schema."
                            })
                            final_res = ollama.chat(
                                model=model,
                                messages=messages,
                                format=schema.model_json_schema(),
                                options={'temperature': temperature}
                            )
                            raw_json_string = final_res['message']['content']
                            parsed_data = json.loads(raw_json_string)
                            data = schema(**parsed_data)
                            
                            prompt_tokens = response.get('prompt_eval_count', 0) + final_res.get('prompt_eval_count', 0)
                            eval_tokens = response.get('eval_count', 0) + final_res.get('eval_count', 0)
                            usage = {
                                "prompt_token_count": prompt_tokens,
                                "candidates_token_count": eval_tokens,
                                "total_token_count": prompt_tokens + eval_tokens
                            }
                            self.total_prompt_tokens += prompt_tokens
                            self.total_candidate_tokens += eval_tokens
                            self.total_tokens += (prompt_tokens + eval_tokens)
                            
                            return AIPromptResult(success=True, error="", data=data, usage_metadata=usage, calculator_calls=calculator_calls)
                        except Exception as e:
                            return AIPromptResult(success=False, error=f"Parsing JSON failed: {e}", calculator_calls=calculator_calls)
                    else:
                        return AIPromptResult(success=True, error="", data=response['message']['content'], calculator_calls=calculator_calls)
                        
            return AIPromptResult(success=False, error="Exceeded maximum tool calling turns.", calculator_calls=calculator_calls)
            
        except Exception as e:
            return AIPromptResult(success=False, error=str(e))
