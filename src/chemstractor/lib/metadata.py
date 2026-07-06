from pydantic import BaseModel, Field
from chemstractor.AI import AI

class PaperMetadata(BaseModel):
    title: str = Field(description="The main title of the academic paper (typically near the top). If not found, use 'Not Found'.")
    authors: list[str] = Field(description="The list of author names of the academic paper. If not found, return an empty list.")
    doi: str | None = Field(None, description="The DOI (Digital Object Identifier) number of the paper (e.g. '10.1021/acs.jced.7b00123'), or 'Not found' if not specified or not found.")
    abstract: str | None = Field(None, description="The abstract of the academic paper summarizing its content. If not found, use 'Not Found'.")


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
    4. The abstract of the academic paper summarizing its content.
    
    If any of these fields cannot be found from the below input, provide the output "Not found" or 
    an empty list if the output requires an output of type list. This list should be empty!

    Paper Content:
    {parsed_markdown[:20000]}
    """


def extract_paper_metadata(parsed_markdown: str) -> PaperMetadataResponse:
    ai = AI.get_instance()
    prompt = get_metadata_prompt(parsed_markdown)
    
    res = ai.prompt(
        prompt=prompt,
        schema=PaperMetadata,
    )
    
    if res.success:
        return PaperMetadataResponse(success=True, error="", data=res.data, usage_metadata=res.usage_metadata)
    else:
        return PaperMetadataResponse(success=False, error=res.error)
