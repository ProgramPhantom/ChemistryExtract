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


class TableFilter(BaseModel):
    contains_scientific_data: bool = Field(
        description=(
            "True if the table or its context contains scientific data resulting from a physical chemistry "
            "experiment, such as a diffusion experiment (e.g., DOSY NMR, NMR, light scattering, etc.). "
            "False if the table does not contain experimental scientific measurements or outcomes."
        )
    )
    contains_diffusion_coeff: bool = Field(
        description=(
            "True if the data specifically contains diffusion coefficients or related diffusion parameters. "
            "Look for columns, rows, headings, or notes indicating diffusion values (e.g., D, D_self, D_0) "
            "with units such as m^2 s^-1, m^2/s, cm^2/s, or similar. False otherwise."
        )
    )
    contains_polymer_diffusion_coeff: bool = Field(
        description=(
            "True if diffusion coefficients are present and at least some of them represent the diffusion "
            "coefficients of polymers (macromolecules, copolymers, block copolymers, etc.). If any polymer "
            "diffusion data is present, this should be True, even if small molecule data is also present. "
            "False otherwise."
        )
    )

class TableCategoryResponse():
    success: bool
    error: str
    contains_diffusion: bool
    contains_scientific_data: bool
    contains_diffusion_coeff: bool
    contains_polymer_diffusion_coeff: bool
    usage_metadata: dict | None

    def __init__(
        self,
        success: bool,
        error: str,
        contains_diffusion: bool,
        contains_scientific_data: bool = False,
        contains_diffusion_coeff: bool = False,
        contains_polymer_diffusion_coeff: bool = False,
        usage_metadata: dict | None = None
    ):
        self.success = success
        self.error = error
        self.contains_diffusion = contains_diffusion
        self.contains_scientific_data = contains_scientific_data
        self.contains_diffusion_coeff = contains_diffusion_coeff
        self.contains_polymer_diffusion_coeff = contains_polymer_diffusion_coeff
        self.usage_metadata = usage_metadata



def get_categorise_prompt(table_string: str) -> str:
    return f"""
    You are a chemistry data classifier. Analyze the following extracted table 
    and its surrounding context. Determine if it contains polymer chemical diffusion coefficient data.
    
    Follow this chain of thought to classify:
    1. Check if the table or its context contains scientific data resulting from a diffusion experiment (such as DOSY NMR, light scattering, etc.).
    2. Check if the table specifically contains diffusion coefficients (look for headings/units indicating m^2 s^-1, cm^2/s, etc.).
    3. Check if these diffusion coefficients correspond to polymers (macromolecules, copolymers, etc.), even if some are small molecules.
    
    Table Data:
    {table_string}
    """


def categorise_table(table_file_path: str, model: AllSupportedModels = "gemini") -> TableCategoryResponse:
    if not os.path.exists(table_file_path):
        return TableCategoryResponse(success=False, error="Table file not found.", contains_diffusion=False)
        
    with open(table_file_path, 'r', encoding='utf-8') as f:
        table_text = f.read()
        
    if model == "gemini":
        model = "gemini-2.5-flash"

    if model in ONLINE_MODELS:
        return categorise_table_gemini(table_text, model)
    elif model in OFFLINE_MODELS:
        return categorise_table_local(table_text, model)

    return TableCategoryResponse(success=False, error="Invalid model", contains_diffusion=False)


def categorise_table_local(table_string: str, model="llama3.1") -> TableCategoryResponse:
    prompt = f"""
    You are a chemistry data classifier. Analyze the following extracted table 
    and its surrounding context. Determine if it contains polymer chemical diffusion coefficient data.
    
    Follow this chain of thought to classify:
    1. Check if the table or its context contains scientific data resulting from a diffusion experiment (such as DOSY NMR, light scattering, etc.).
    2. Check if the table specifically contains diffusion coefficients (look for headings/units indicating m^2 s^-1, cm^2/s, etc.).
    3. Check if these diffusion coefficients correspond to polymers (macromolecules, copolymers, etc.), even if some are small molecules.
    
    Table Data:
    {table_string}
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            format=TableFilter.model_json_schema(),
            options={'temperature': 0.0} 
        )
        raw_json_string = response['message']['content']
        parsed_data = json.loads(raw_json_string)
        contains_diff = (
            parsed_data.get('contains_scientific_data', False) and
            parsed_data.get('contains_diffusion_coeff', False) and
            parsed_data.get('contains_polymer_diffusion_coeff', False)
        )
        return TableCategoryResponse(
            success=True,
            error="",
            contains_diffusion=contains_diff,
            contains_scientific_data=parsed_data.get('contains_scientific_data', False),
            contains_diffusion_coeff=parsed_data.get('contains_diffusion_coeff', False),
            contains_polymer_diffusion_coeff=parsed_data.get('contains_polymer_diffusion_coeff', False)
        )
    except Exception as e:
        return TableCategoryResponse(success=False, error=str(e), contains_diffusion=False)


def categorise_table_gemini(table_string: str, model: str = 'gemini-2.5-flash') -> TableCategoryResponse:
    client = genai.Client(api_key=API_KEY)
    prompt = get_categorise_prompt(table_string)
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=TableFilter,
                temperature=0.0, 
            ),
        )
        parsed = response.parsed
        contains_diff = (
            parsed.contains_scientific_data and
            parsed.contains_diffusion_coeff and
            parsed.contains_polymer_diffusion_coeff
        )
        usage = None
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            usage = {
                "prompt_token_count": response.usage_metadata.prompt_token_count,
                "candidates_token_count": response.usage_metadata.candidates_token_count,
                "total_token_count": response.usage_metadata.total_token_count
            }
    except Exception as e:
        return TableCategoryResponse(success=False, error=str(e), contains_diffusion=False)
    
    return TableCategoryResponse(
        success=True,
        error="",
        contains_diffusion=contains_diff,
        contains_scientific_data=parsed.contains_scientific_data,
        contains_diffusion_coeff=parsed.contains_diffusion_coeff,
        contains_polymer_diffusion_coeff=parsed.contains_polymer_diffusion_coeff,
        usage_metadata=usage
    )




    
if __name__ == '__main__':

    print(API_KEY)