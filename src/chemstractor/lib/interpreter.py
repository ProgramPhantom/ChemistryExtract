import math
from typing import Optional, List
from pydantic import BaseModel, Field
from chemstractor.AI import AI


# 1. Define the schema for a SINGLE equation/row (Mark-Houwink)
class MarkHouwinkEntry(BaseModel):
    polymer_name: str = Field(description="The name or acronym of the polymer.")
    solvent: str = Field(description="The solvent used.")
    temperature_k: Optional[float] = Field(None, description="Temperature in Kelvin, if stated in the text or table.")
    raw_K_value: float = Field(description="The raw number representing the pre-exponential factor K.")
    K_transformation: str = Field(description="Transformation applied to K. Options: 'none', 'log', 'ln', 'unknown'.")
    K_value: float = Field(description="The standard, calculated/converted value of K in standard units (mL/g). If K_transformation is 'log', K_value = 10^raw_K_value. If 'ln', K_value = e^raw_K_value. If 'none', K_value = raw_K_value.")
    raw_a_value: float = Field(description="The raw number representing the scaling exponent a.")
    a_transformation: str = Field(description="Transformation applied to a. Options: 'none', 'reciprocal', 'unknown'.")
    a_value: float = Field(description="The standard, calculated/converted value of the exponent a. If a_transformation is 'reciprocal', a_value = 1/raw_a_value. If 'none', it is raw_a_value.")


# 2. Define the schema for a SINGLE equation/row (Flory)
class FloryEntry(BaseModel):
    polymer_name: str = Field(description="The name or acronym of the polymer.")
    solvent: str = Field(description="The solvent used.")
    temperature_k: Optional[float] = Field(None, description="Temperature in Kelvin, if stated in the text or table.")
    raw_v_value: float = Field(description="The raw number representing the Flory coefficient/exponent v (often represented as nu or v).")
    v_transformation: str = Field(description="Transformation applied to v. Options: 'none', 'reciprocal', 'unknown'.")
    v_value: float = Field(description="The standard, calculated/converted value of the coefficient v. If v_transformation is 'reciprocal', v_value = 1/raw_v_value. If 'none', it is raw_v_value.")
    raw_c_value: float = Field(description="The raw number representing the Flory constant c (often represented as C or c).")
    c_transformation: str = Field(description="Transformation applied to c. Options: 'none', 'log', 'ln', 'unknown'.")
    c_value: float = Field(description="The standard, calculated/converted value of the constant c. If c_transformation is 'log', c_value = 10^raw_c_value. If 'ln', c_value = e^raw_c_value. If 'none', c_value = raw_c_value.")


# 3. Define the wrapper schema for the ENTIRE TABLE
class TableExtraction(BaseModel):
    is_mark_houwink_data: bool = Field(
        description="True if the table contains Mark-Houwink equation parameters (K and a). False otherwise."
    )
    is_flory_data: bool = Field(
        description="True if the table contains Flory coefficient and constant parameters (v and c). False otherwise."
    )
    entries: List[MarkHouwinkEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Mark-Houwink row in the table. Do not skip any rows. Leave empty if the table does not contain Mark-Houwink parameters."
    )
    flory_entries: List[FloryEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Flory parameter row in the table. Do not skip any rows. Leave empty if the table does not contain Flory parameters."
    )


class TableInterpretationResponse:
    success: bool
    error: str
    data: TableExtraction | None
    usage_metadata: dict | None
    calculator_calls: List[dict]

    def __init__(self, success: bool, error: str = "", data: TableExtraction | None = None, usage_metadata: dict | None = None, calculator_calls: List[dict] = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata
        self.calculator_calls = calculator_calls or []


def calculate_math(expression: str) -> float:
    """
    Evaluates a mathematical expression and returns the result. 
    Use this for ANY algebra, inversion, logarithms, or multiplication.
    """
    try:
        # Define allowed variables/functions from math module
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        # Add basic functions
        allowed_names.update({
            'abs': abs,
            'float': float,
            'int': int,
            'pow': pow,
            'round': round,
        })
        # Evaluate safely
        return float(eval(expression, {"__builtins__": None}, allowed_names))
    except Exception as e:
        return f"Error computing {expression}: {e}"


def get_interpret_prompt(table_text: str, title: str | None = None, abstract: str | None = None, cat_data: dict | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"
        
    extraction_target = []
    if cat_data:
        if cat_data.get("contains_mark_houwink_parameters", False):
            extraction_target.append("Mark-Houwink parameters (K and a)")
        if cat_data.get("contains_flory_parameters", False):
            extraction_target.append("Flory parameters (coefficient v and constant c)")
            
    if not extraction_target:
        extraction_target = ["Mark-Houwink parameters (K and a) and/or Flory parameters (coefficient v and constant c)"]
        
    target_str = " and ".join(extraction_target)

    return f"""
    You are a chemistry data converter. Analyze the following extracted table and its surrounding context.
    Your task is to extract {target_str} for each row where applicable.
    
    For Mark-Houwink entries (if extracting):
    Extract the polymer name, solvent, temperature, and Mark-Houwink coefficients (K and a).
    
    For Flory entries (if extracting):
    Extract the polymer name, solvent, temperature, and Flory parameters (coefficient v and constant c).
    
    If the coefficients/parameters in the table are transformed (for example, if they are listed as log(X), ln(X), 1/X, or reciprocal of X),
    you MUST call the `calculate_math` tool to compute the standard/converted values.
    Do NOT do any math, logarithm, exponentiation, or reciprocal calculation in your head. Use the `calculate_math` tool!
    
    {context_str}
    
    Table Data:
    {table_text}
    """


def interpret_table(table_text: str, title: str | None = None, abstract: str | None = None, cat_data: dict | None = None) -> TableInterpretationResponse:
    ai = AI.get_instance()
    prompt = get_interpret_prompt(table_text, title=title, abstract=abstract, cat_data=cat_data)
    system_instruction = (
        "You are a precise chemistry data extractor. You must NEVER do math in your head. "
        "If you need to invert a number, take a logarithm, exponentiate, or multiply to find the standard parameters, "
        "you MUST use the calculate_math tool."
    )
    
    res = ai.prompt(
        prompt=prompt,
        schema=TableExtraction,
        tools=[calculate_math],
        system_instruction=system_instruction
    )
    
    if res.success:
        return TableInterpretationResponse(
            success=True,
            data=res.data,
            usage_metadata=res.usage_metadata,
            calculator_calls=res.calculator_calls
        )
    else:
        return TableInterpretationResponse(
            success=False,
            error=res.error,
            calculator_calls=res.calculator_calls
        )
