from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import ollama
import json
import os


load_dotenv()
API_KEY = os.getenv('API_KEY')


class TableFilter(BaseModel):
    contains_diffusion_data: bool = Field(
        description="True if the table or context contains diffusion coefficients or related diffusion data. False otherwise."
    )

class TableCategoryResponse():
    success: bool
    error: str
    contains_diffusion: bool

    def __init__(self, success: bool, error: str, contains_diffusion: bool):
        self.success = success
        self.error = error
        self.contains_diffusion = contains_diffusion


def categorise_table(table_file_path: str, model="gemini") -> TableCategoryResponse:
    if not os.path.exists(table_file_path):
        return TableCategoryResponse(success=False, error="Table file not found.", contains_diffusion=False)
        
    with open(table_file_path, 'r', encoding='utf-8') as f:
        table_text = f.read()
        
    if model == "gemini":
        return categorise_table_gemini(table_text)
    elif model == "llama3.1":
        return categorise_table_local(table_text, model)

    return TableCategoryResponse(success=False, error="Invalid model", contains_diffusion=False)


def categorise_table_local(table_string: str, model="llama3.1") -> TableCategoryResponse:
    prompt = f"""
    You are a chemistry data classifier. Analyze the following extracted table 
    and its surrounding context. Determine if it contains chemical diffusion coefficient data 
    (such as self-diffusion coefficients, mutual diffusion coefficients, tracer diffusion 
    coefficients, polymer diffusion data, or related diffusion data).
    
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
        contains_diff = parsed_data.get('contains_diffusion_data', False)
        return TableCategoryResponse(success=True, error="", contains_diffusion=contains_diff)
    except Exception as e:
        return TableCategoryResponse(success=False, error=str(e), contains_diffusion=False)


def categorise_table_gemini(table_string: str) -> TableCategoryResponse:
    client = genai.Client(api_key=API_KEY)
    
    prompt = f"""
    You are a chemistry data classifier. Analyze the following extracted table 
    and its surrounding context. Determine if it contains chemical diffusion coefficient data 
    (such as self-diffusion coefficients, mutual diffusion coefficients, tracer diffusion 
    coefficients, polymer diffusion data, or related diffusion data).
    
    Table Data:
    {table_string}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=TableFilter,
                temperature=0.0, 
            ),
        )
    except Exception as e:
        return TableCategoryResponse(success=False, error=str(e), contains_diffusion=False)
    
    return TableCategoryResponse(success=True, error="", contains_diffusion=response.parsed.contains_diffusion_data)




    
if __name__ == '__main__':

    print(API_KEY)