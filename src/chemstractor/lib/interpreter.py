import math
from typing import Optional, List
from pydantic import BaseModel, Field
from chemstractor.AI import AI


# 1. Define the schema for a SINGLE equation/row
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


# 2. Define the wrapper schema for the ENTIRE TABLE
class TableExtraction(BaseModel):
    is_mark_houwink_data: bool = Field(
        description="True if the table contains Mark-Houwink equation parameters. False if it is raw data points or unrelated."
    )
    entries: List[MarkHouwinkEntry] = Field(
        description="A list containing one entry for EVERY valid row in the table. Do not skip any rows."
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


def get_interpret_prompt(table_text: str, title: str | None = None, abstract: str | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"
        
    return f"""
    You are a chemistry data converter. Analyze the following extracted table and its surrounding context.
    Your task is to extract the polymer name, solvent, temperature, and Mark-Houwink coefficients (K and a) for each row.
    
    If the K or a coefficients in the table are transformed (for example, if they are listed as log(K), ln(K), or 1/a, or reciprocal of a),
    you MUST call the `calculate_math` tool to compute the standard/converted K and a values.
    Do NOT do any math, logarithm, exponentiation, or reciprocal calculation in your head. Use the `calculate_math` tool!
    
    {context_str}
    
    Table Data:
    {table_text}
    """


def interpret_table(table_text: str, title: str | None = None, abstract: str | None = None) -> TableInterpretationResponse:
    ai = AI.get_instance()
    prompt = get_interpret_prompt(table_text, title=title, abstract=abstract)
    system_instruction = (
        "You are a precise chemistry data extractor. You must NEVER do math in your head. "
        "If you need to invert a number, take a logarithm, exponentiate, or multiply to find the standard Mark-Houwink parameters, "
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
