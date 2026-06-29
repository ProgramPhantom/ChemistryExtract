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


def summarise_table_conditions_gemini(table_summary: str) -> TableSummaryResponse:
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure) to "Not applicable" and return an empty list for chemicals and other_statistics.
    
    Table Summary:
    {table_summary}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
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


class PaperMetadata(BaseModel):
    title: str = Field(description="The main title of the academic paper (typically near the top). If not found, use 'Not Found'.")
    authors: list[str] = Field(description="The list of author names of the academic paper. If not found, return an empty list.")
    doi: str | None = Field(None, description="The DOI (Digital Object Identifier) number of the paper (e.g. '10.1021/acs.jced.7b00123'), or 'Not applicable' if not specified or not found.")


class PaperMetadataResponse:
    success: bool
    error: str
    data: PaperMetadata | None

    def __init__(self, success: bool, error: str, data: PaperMetadata | None = None):
        self.success = success
        self.error = error
        self.data = data


def extract_paper_metadata(parsed_markdown: str, model: str = "gemini") -> PaperMetadataResponse:
    if model == "gemini":
        return extract_paper_metadata_gemini(parsed_markdown)
    elif model == "llama3.1":
        return extract_paper_metadata_local(parsed_markdown, model)

    return PaperMetadataResponse(success=False, error="Invalid model")


def extract_paper_metadata_local(parsed_markdown: str, model: str = "llama3.1") -> PaperMetadataResponse:
    prompt = f"""
    You are an academic paper metadata extractor. Analyze the following parsed academic paper text (in Markdown format).
    Extract:
    1. The main title of the paper (typically at the very beginning of the document).
    2. The names of the authors.
    3. The DOI (Digital Object Identifier) number of the paper.
    
    If any of these fields are not found or not specified in the text, use "Not found" for string fields and an empty list for the authors.
    
    Paper Content:
    {parsed_markdown[:20000]}
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            format=PaperMetadata.model_json_schema(),
            options={'temperature': 0.0}
        )
        raw_json_string = response['message']['content']
        parsed_data = json.loads(raw_json_string)
        data = PaperMetadata(**parsed_data)
        return PaperMetadataResponse(success=True, error="", data=data)
    except Exception as e:
        return PaperMetadataResponse(success=False, error=str(e))


def extract_paper_metadata_gemini(parsed_markdown: str) -> PaperMetadataResponse:
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"""
    You are an academic paper metadata extractor. Analyze the following parsed academic paper text (in Markdown format).
    Extract:
    1. The main title of the paper (typically at the very beginning of the document).
    2. The names of the authors.
    3. The DOI (Digital Object Identifier) number of the paper.
    
    If any of these fields are not found or not specified in the text, use "Not applicable" for string fields and an empty list for the authors.
    
    Paper Content:
    {parsed_markdown[:20000]}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=PaperMetadata,
                temperature=0.0,
            ),
        )
        return PaperMetadataResponse(success=True, error="", data=response.parsed)
    except Exception as e:
        return PaperMetadataResponse(success=False, error=str(e))
