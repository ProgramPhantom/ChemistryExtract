from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import ollama
import json
import os

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
        description="The temperature(s) at which the experiment was conducted (e.g. '298.15 K', '25 °C'), or 'Not applicable' if not specified or not experimental data."
    )
    pressure: str | None = Field(
        None,
        description="The pressure(s) at which the experiment was conducted (e.g. '1 atm', '101.3 kPa'), or 'Not applicable' if not specified or not experimental data."
    )
    solvent: str | None = Field(
        None,
        description="The solvent or medium used in the experiment (e.g. 'water', 'ethanol'), or 'Not applicable' if not specified or not experimental data."
    )
    other_statistics: list[ExtraStatistic] = Field(
        default_factory=list,
        description="Other key experimental variables, parameters, or statistics found in the table or context (e.g. pH, concentration, density, activation energy) represented as list of key-value objects. If none are found or if not applicable, return an empty list."
    )

class TableSummaryResponse:
    success: bool
    error: str
    data: ExperimentalConditions | None

    def __init__(self, success: bool, error: str, data: ExperimentalConditions | None = None):
        self.success = success
        self.error = error
        self.data = data


def summarise_table_conditions(table_summary: str, model: str = "gemini") -> TableSummaryResponse:
    if model == "gemini":
        return summarise_table_conditions_gemini(table_summary)
    elif model == "llama3.1":
        return summarise_table_conditions_local(table_summary, model)

    return TableSummaryResponse(success=False, error="Invalid model")


def summarise_table_conditions_local(table_summary: str, model: str = "llama3.1") -> TableSummaryResponse:
    prompt = f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure, solvent) to "Not applicable" and return an empty list for other_statistics.
    
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


def summarise_table_conditions_gemini(table_summary: str) -> TableSummaryResponse:
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure, solvent) to "Not applicable" and return an empty list for other_statistics.
    
    Table Summary:
    {table_summary}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExperimentalConditions,
                temperature=0.0,
            ),
        )
        return TableSummaryResponse(success=True, error="", data=response.parsed)
    except Exception as e:
        return TableSummaryResponse(success=False, error=str(e))
