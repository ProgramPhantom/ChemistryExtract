from typing import Literal
from pydantic import BaseModel, Field
from chemstractor.AI import AI


class TableFilter(BaseModel):
    contains_experimental_data: bool = Field(
        description=(
            "True if the table contains scientific data resulting from a physical chemistry "
            "experiment, such as a diffusion experiment (e.g., DOSY NMR, NMR, light scattering, etc.). "
            "This should only be marked true if the data is from a scientific reading or measurement, "
            "or from the literature. This should not be true if the data is summary statistics of data,"
            "standard errors or other non-empirical data."
            "False if the table does not contain experimental scientific measurements or outcomes."
        )
    )
    contains_diffusion_coeff: Literal["raw", "coeff", "unsure", "N/A"] = Field(
        description=(
            "The type of diffusion data present in the table. "
            "Select 'raw' if the table contains empirical recorded diffusion coefficients for polymers "
            "at different atomic masses (or molecular weights). "
            "Select 'coeff' if the table directly provides the coefficients of the Mark-Houwink equation "
            "(or some transformation of those coefficients, e.g., K and alpha parameters). "
            "Select 'unsure' if you are unsure which one it is. "
            "Select 'N/A' if the table does not contain diffusion coefficient data or related parameters."
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
    contains_diffusion_coeff: str
    contains_polymer_diffusion_coeff: bool
    usage_metadata: dict | None

    def __init__(
        self,
        success: bool,
        error: str,
        contains_diffusion: bool,
        contains_scientific_data: bool = False,
        contains_diffusion_coeff: str = "N/A",
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



def get_categorise_prompt(table_string: str, title: str | None = None, abstract: str | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"

    return f"""
    You are a chemistry data classifier. Analyze the following extracted table 
    and its surrounding context. Determine if it contains polymer chemical diffusion coefficient data.
    
    Follow this chain of thought to classify:
    1. Check if the table or its context contains scientific data resulting from a diffusion experiment (such as DOSY NMR, light scattering, etc.).
    2. Decide between two types of diffusion data:
       - 'raw': empirical recorded diffusion coefficients for each polymer at different atomic masses (molecular weights).
       - 'coeff': the table directly provides the coefficients of the Mark-Houwink equation (or some transformation of those coefficients, e.g. K and a/alpha parameters).
       If you are unsure, select 'unsure'. If the table does not contain diffusion coefficient data, select 'N/A'.
    3. Check if these diffusion coefficients correspond to polymers (macromolecules, copolymers, etc.), even if some are small molecules.
    
    {context_str}

    Table Data:
    {table_string}
    """


def categorise_table(table_text: str, title: str | None = None, abstract: str | None = None) -> TableCategoryResponse:
    ai = AI.get_instance()
    prompt = get_categorise_prompt(table_text, title=title, abstract=abstract)
    
    res = ai.prompt(
        prompt=prompt,
        schema=TableFilter,
    )
    
    if res.success:
        parsed = res.data
        contains_diff = (
            parsed.contains_experimental_data and
            parsed.contains_polymer_diffusion_coeff
        )
        return TableCategoryResponse(
            success=True,
            error="",
            contains_diffusion=contains_diff,
            contains_scientific_data=parsed.contains_experimental_data,
            contains_diffusion_coeff=parsed.contains_diffusion_coeff,
            contains_polymer_diffusion_coeff=parsed.contains_polymer_diffusion_coeff,
            usage_metadata=res.usage_metadata
        )
    else:
        return TableCategoryResponse(success=False, error=res.error, contains_diffusion=False)