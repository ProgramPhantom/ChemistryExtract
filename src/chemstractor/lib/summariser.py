from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import sys
import ollama
import json
import os

from chemstractor.models import AllSupportedModels, ONLINE_MODELS, OFFLINE_MODELS

load_dotenv()
API_KEY = os.getenv('API_KEY')

class ExtraStatistic(BaseModel):
    name: str = Field(description="The name of the variable, parameter, or statistic (e.g. 'pH', 'concentration', 'density').")
    value: str = Field(description="The value of this parameter/statistic.")

class ExperimentalConditions(BaseModel):
    description: str = Field(
        description="A paragraph describing the experimental conditions under which the data in the table was gathered. Use 'Not applicable' if the table does not present experimental data or the context does not specify conditions."
    )
    temperature: str | None = Field(
        None,
        description="The temperature(s) at which the experiment was conducted (e.g. '298.15 K', '25 °C'), or 'Not applicable' if not experimental data or 'Not found' if not specified"
    )
    pressure: str | None = Field(
        None,
        description="The pressure(s) at which the experiment was conducted (e.g. '1 atm', '101.3 kPa'), or 'Not applicable' if not experimental data or 'Not found' if not specified"
    )
    chemicals: list[str] = Field(
        default_factory=list,
        description="The list of chemicals or substances involved in the experiment or table (e.g. reagents, solvents, reactants, products), or an empty list if not applicable or none specified."
    )
    other_statistics: list[ExtraStatistic] = Field(
        default_factory=list,
        description="Other key experimental variables, parameters, or statistics found in the table or context (e.g. pH, concentration, density, activation energy) represented as list of key-value objects. If none are found or if not applicable, return an empty list."
    )

class TableSummaryResponse:
    success: bool
    error: str
    data: ExperimentalConditions | None
    usage_metadata: dict | None

    def __init__(self, success: bool, error: str, data: ExperimentalConditions | None = None, usage_metadata: dict | None = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata


def summarise_table_conditions(table_summary: str, model: AllSupportedModels = "gemini-2.5-flash") -> TableSummaryResponse:
    if model in ONLINE_MODELS:
        return summarise_table_conditions_gemini(table_summary, model)
    elif model in OFFLINE_MODELS:
        return summarise_table_conditions_local(table_summary, model)

    return TableSummaryResponse(success=False, error="Invalid model")


def summarise_table_conditions_local(table_summary: str, model: str = "llama3.1") -> TableSummaryResponse:
    prompt = f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure) to "Not applicable" and return an empty list for chemicals and other_statistics.
    
    Table Summary:
    {table_summary}
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            format=ExperimentalConditions.model_json_schema(),
            options={'temperature': 0.0}
        )
        raw_json_string = response['message']['content']
        parsed_data = json.loads(raw_json_string)
        data = ExperimentalConditions(**parsed_data)
        return TableSummaryResponse(success=True, error="", data=data)
    except Exception as e:
        return TableSummaryResponse(success=False, error=str(e))


def get_summarise_prompt(table_summary: str) -> str:
    return f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure) to "Not applicable" and return an empty list for chemicals and other_statistics.
    
    Table Summary:
    {table_summary}
    """


def summarise_table_conditions_gemini(table_summary: str, model: str = 'gemini-2.5-flash') -> TableSummaryResponse:
    client = genai.Client(api_key=API_KEY)
    prompt = get_summarise_prompt(table_summary)
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExperimentalConditions,
                temperature=0.0,
            ),
        )
        usage = None
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            usage = {
                "prompt_token_count": response.usage_metadata.prompt_token_count,
                "candidates_token_count": response.usage_metadata.candidates_token_count,
                "total_token_count": response.usage_metadata.total_token_count
            }
        return TableSummaryResponse(success=True, error="", data=response.parsed, usage_metadata=usage)
    except Exception as e:
        return TableSummaryResponse(success=False, error=str(e))



