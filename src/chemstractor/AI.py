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
OfflineModels = Literal["llama3.1", "llama3"]
AllSupportedModels = Union[OnlineModels, OfflineModels]

ONLINE_MODELS = list(pricing_matrix.keys())
OFFLINE_MODELS = list(get_args(OfflineModels))


class AIPromptResult:
    """Standardized response from prompt calls, containing success status, parsed data, and token usage."""
    def __init__(self, success: bool, error: str = "", data: BaseModel = None, usage_metadata: dict = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata


class AI:
    pricing_matrix = pricing_matrix
    ONLINE_MODELS = ONLINE_MODELS
    OFFLINE_MODELS = OFFLINE_MODELS
    DEFAULT_MODEL = "gemini-2.5-flash"
    
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

    def prompt(self, prompt: str, schema: type[BaseModel], model: AllSupportedModels = None, temperature: float = 0.0) -> AIPromptResult:
        """General prompt endpoint which routes requests to either Gemini or local Ollama depending on the model."""
        if model is None:
            model = self.selected_model
            
        if model in self.ONLINE_MODELS:
            return self._prompt_gemini(prompt, schema, model, temperature)
        elif model in self.OFFLINE_MODELS:
            return self._prompt_local(prompt, schema, model, temperature)
        else:
            return AIPromptResult(success=False, error=f"Unsupported model: {model}")

    def _prompt_gemini(self, prompt: str, schema: type[BaseModel], model: str, temperature: float) -> AIPromptResult:
        if not self.client:
            self.api_key = os.getenv('API_KEY')
            if self.api_key:
                self.client = genai.Client(api_key=self.api_key)
            else:
                return AIPromptResult(success=False, error="API_KEY environment variable is not set.")
                
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema,
                    temperature=temperature,
                ),
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
        except Exception as e:
            return AIPromptResult(success=False, error=str(e))

    def _prompt_local(self, prompt: str, schema: type[BaseModel], model: str, temperature: float) -> AIPromptResult:
        try:
            response = ollama.chat(
                model=model,
                messages=[{'role': 'user', 'content': prompt}],
                format=schema.model_json_schema(),
                options={'temperature': temperature}
            )
            raw_json_string = response['message']['content']
            parsed_data = json.loads(raw_json_string)
            data = schema(**parsed_data)
            
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
        except Exception as e:
            return AIPromptResult(success=False, error=str(e))
