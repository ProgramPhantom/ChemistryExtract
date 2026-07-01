from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import ollama
import json
import os

from chemstractor.models import AllSupportedModels, ONLINE_MODELS, OFFLINE_MODELS

load_dotenv()
API_KEY = os.getenv('API_KEY')

class PaperMetadata(BaseModel):
    title: str = Field(description="The main title of the academic paper (typically near the top). If not found, use 'Not Found'.")
    authors: list[str] = Field(description="The list of author names of the academic paper. If not found, return an empty list.")
    doi: str | None = Field(None, description="The DOI (Digital Object Identifier) number of the paper (e.g. '10.1021/acs.jced.7b00123'), or 'Not found' if not specified or not found.")


class PaperMetadataResponse:
    success: bool
    error: str
    data: PaperMetadata | None
    usage_metadata: dict | None

    def __init__(self, success: bool, error: str, data: PaperMetadata | None = None, usage_metadata: dict | None = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata



def get_metadata_prompt(parsed_markdown: str) -> str:
    return f"""
    You are an academic paper metadata extractor. Analyze the following parsed academic paper text (in Markdown format).
    Extract:
    1. The main title of the paper (typically at the very beginning of the document).
    2. The names of the authors.
    3. The DOI (Digital Object Identifier) number of the paper.
    
    If any of these fields are not found or not specified in the text, use "Not applicable" for string fields and an empty list for the authors.
    
    Paper Content:
    {parsed_markdown[:20000]}
    """


def extract_paper_metadata(parsed_markdown: str, model: AllSupportedModels = "gemini-2.5-flash") -> PaperMetadataResponse:
    if model in ONLINE_MODELS:
        return extract_paper_metadata_gemini(parsed_markdown, model)
    elif model in OFFLINE_MODELS:
        return extract_paper_metadata_local(parsed_markdown, model)

    return PaperMetadataResponse(success=False, error="Invalid model")


def extract_paper_metadata_local(parsed_markdown: str, model: OFFLINE_MODELS = "llama3.1") -> PaperMetadataResponse:
    prompt = get_metadata_prompt(parsed_markdown)
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


def extract_paper_metadata_gemini(parsed_markdown: str, model: ONLINE_MODELS = 'gemini-2.5-flash') -> PaperMetadataResponse:
    client = genai.Client(api_key=API_KEY)
    prompt = get_metadata_prompt(parsed_markdown)
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=PaperMetadata,
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
        return PaperMetadataResponse(success=True, error="", data=response.parsed, usage_metadata=usage)
    except Exception as e:
        return PaperMetadataResponse(success=False, error=str(e))
