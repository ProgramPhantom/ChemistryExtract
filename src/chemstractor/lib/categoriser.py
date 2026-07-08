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
    contains_raw_diffusion_data: bool = Field(
        description=(
            "True if the table contains raw empirical recorded diffusion coefficient data (for polymers "
            "at different atomic masses or molecular weights). False otherwise."
        )
    )
    contains_mark_houwink_parameters: bool = Field(
        description=(
            "True if the table contains the coefficients of the Mark-Houwink equation (or some "
            "transformation of those coefficients, e.g. K and alpha/a parameters). False otherwise."
        )
    )
    contains_flory_parameters: bool = Field(
        description=(
            "True if the table contains Flory parameters and/or constants (such as the Flory exponent "
            "or constant, e.g., the Flory coefficient or parameter which are often written in different ways, "
            "such as being represented as v or b). False otherwise."
        )
    )
    contains_polymer_diffusion_coeff: bool = Field(
        description=(
            "True if diffusion coefficients or parameters are present and at least some of them represent the diffusion "
            "coefficients or parameters of polymers. If any polymer "
            "diffusion/parameter data is present, this should be True, even if small molecule data is also present. "
            "False otherwise."
        )
    )

class TableCategoryResponse():
    success: bool
    error: str
    flagged: bool
    contains_scientific_data: bool
    contains_raw_diffusion_data: bool
    contains_mark_houwink_parameters: bool
    contains_flory_parameters: bool
    contains_polymer_diffusion_coeff: bool
    usage_metadata: dict | None

    def __init__(
        self,
        success: bool,
        error: str,
        flagged: bool,
        contains_scientific_data: bool = False,
        contains_raw_diffusion_data: bool = False,
        contains_mark_houwink_parameters: bool = False,
        contains_flory_parameters: bool = False,
        contains_polymer_diffusion_coeff: bool = False,
        usage_metadata: dict | None = None
    ):
        self.success = success
        self.error = error
        self.flagged = flagged
        self.contains_scientific_data = contains_scientific_data
        self.contains_raw_diffusion_data = contains_raw_diffusion_data
        self.contains_mark_houwink_parameters = contains_mark_houwink_parameters
        self.contains_flory_parameters = contains_flory_parameters
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
    and its surrounding context. Determine if it contains polymer chemical diffusion coefficient data or parameters.
    
    Follow this chain of thought to classify:
    1. Check if the table or its context contains scientific data resulting from a physical chemistry experiment (such as DOSY NMR, light scattering, etc.).
    2. Determine if the data contains either:
       - raw diffusion coefficient data (empirical recorded diffusion coefficients for each polymer at different atomic masses or molecular weights).
       - Mark-Houwink parameters (e.g. K and a/alpha parameters, or some transformation of those coefficients).
       - Flory (Florey) parameters and/or constants (such as the Flory exponent or constant, which are often written in different ways, e.g. the Flory coefficient being represented as v or b).
    3. Check if these diffusion coefficients or parameters correspond to polymers (macromolecules, copolymers, etc.), even if some are small molecules.
    
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
            parsed.contains_polymer_diffusion_coeff and
            (
                parsed.contains_raw_diffusion_data or
                parsed.contains_mark_houwink_parameters or
                parsed.contains_flory_parameters
            )
        )
        return TableCategoryResponse(
            success=True,
            error="",
            flagged=contains_diff,
            contains_scientific_data=parsed.contains_experimental_data,
            contains_raw_diffusion_data=parsed.contains_raw_diffusion_data,
            contains_mark_houwink_parameters=parsed.contains_mark_houwink_parameters,
            contains_flory_parameters=parsed.contains_flory_parameters,
            contains_polymer_diffusion_coeff=parsed.contains_polymer_diffusion_coeff,
            usage_metadata=res.usage_metadata
        )
    else:
        return TableCategoryResponse(success=False, error=res.error, flagged=False)