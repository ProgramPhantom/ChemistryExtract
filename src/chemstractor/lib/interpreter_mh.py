import math
from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, Field
from chemstractor.AI import AI


# Define the schema for a SINGLE equation/row (Mark-Houwink)
class MarkHouwinkEntry(BaseModel):
    polymer_name: str = Field(description="The name or acronym of the polymer.")
    solvent: str = Field(description="The solvent used.")
    temperature_k: Optional[float] = Field(None, description="Temperature in Kelvin, if stated in the text or table.")
    raw_K_value: float = Field(description="The raw number representing the pre-exponential factor K.")
    K_transformation: str = Field(description="Transformation applied to K. E.g. 'none', 'log', 'ln', '10**-8', 'unknown', or any custom multiplier/scaling expression.")
    K_value: float = Field(description="The standard, calculated/converted value of K in standard units (mL/g). If K is scaled or transformed in the table (e.g. log, ln, or multiplied by a factor of 10), you MUST call the calculate_math tool to compute the standard value and store that returned result here. If no transformation is applied, K_value = raw_K_value.")
    raw_a_value: float = Field(description="The raw number representing the scaling exponent a.")
    a_transformation: str = Field(description="Transformation applied to a. E.g. 'none', 'reciprocal', 'unknown', or any custom scaling expression.")
    a_value: float = Field(description="The standard, calculated/converted value of the exponent a. If a is scaled or transformed in the table (e.g. reciprocal 1/a), you MUST call the calculate_math tool to compute the standard value and store that returned result here. If no transformation is applied, a_value = raw_a_value.")


# Define the extraction schema for Mark-Houwink parameters
class MarkHouwinkExtraction(BaseModel):
    is_mark_houwink_data: bool = Field(
        description="True if the table contains Mark-Houwink equation parameters (K and a). False otherwise."
    )
    mh_entries: List[MarkHouwinkEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Mark-Houwink row in the table. Do not skip any rows."
    )


class TableInterpretationResponse:
    success: bool
    error: str
    data: MarkHouwinkExtraction | None
    usage_metadata: dict | None
    calculator_calls: List[dict]

    def __init__(self, success: bool, error: str = "", data: MarkHouwinkExtraction | None = None, usage_metadata: dict | None = None, calculator_calls: List[dict] = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata
        self.calculator_calls = calculator_calls or []


def calculate_math(expression: str) -> float:
    """
    Evaluates a mathematical expression and returns the result as a standard decimal string.
    Use this for ANY algebra, inversion, logarithms, or multiplication.
    
    Supported functions:
    - log10(x) or lg(x): log base 10
    - log(x): natural log (ln)
    - exp(x): e^x
    - sqrt(x): square root
    - pow(x, y) or x**y: exponentiation
    - Basic operators: +, -, *, /, parenthesis
    
    CRITICAL: The expression must contain ONLY numbers and operators/functions. 
    Do NOT include variable names (such as 'c', 'K', 'a', 'v', or polymer names) in the expression. 
    You must substitute the actual extracted raw numerical value into the expression.
    For example:
    - Correct: "10**-2.20882" or "10**2.20882"
    - Incorrect: "10**c" or "lg(c)"
    """
    try:
        # Define allowed variables/functions from math module
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        # Add basic functions and lg mapping
        allowed_names.update({
            'abs': abs,
            'float': float,
            'int': int,
            'pow': pow,
            'round': round,
            'lg': math.log10,
        })
        # Evaluate safely
        val = float(eval(expression, {"__builtins__": None}, allowed_names))
        return f"{Decimal(str(val)).normalize():f}"
    except Exception as e:
        return f"Error computing {expression}: {e}"


def get_mark_houwink_interpret_prompt(table_text: str, title: str | None = None, abstract: str | None = None, formulae: List[str] | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"
    if formulae:
        context_str += "\n    Extracted Mathematical Formulae:\n" + "\n".join(f"    - {formula}" for formula in formulae)
        
    return f"""
    You are a chemistry data converter. Analyze the following extracted table and its surrounding context.
    Your task is to extract Mark-Houwink equation parameters (K and a) for each row where applicable.
    
    For Mark-Houwink entries:
    Extract the polymer name, solvent, temperature, and Mark-Houwink coefficients (K and a).
    
    If the K or a coefficients in the table are transformed (for example, if they are listed as log(K), ln(K), or 1/a, or reciprocal of a),
    you MUST call the `calculate_math` tool to compute the standard/converted K and a values.
    Do NOT do any math, logarithm, exponentiation, or reciprocal calculation in your head. Use the `calculate_math` tool!
    
    {context_str}
    
    Table Data:
    {table_text}
    """


def interpret_mh_table(table_text: str, title: str | None = None, abstract: str | None = None, formulae: List[str] | None = None) -> TableInterpretationResponse:
    ai = AI.get_instance()
    
    mh_prompt = get_mark_houwink_interpret_prompt(table_text, title=title, abstract=abstract, formulae=formulae)
    mh_system_instruction = (
        "You are a precise chemistry data extractor. You must NEVER do math in your head. "
        "If any parameter is transformed or scaled in the table (e.g. log, ln, reciprocal, or a power of 10 multiplier like 10^-8), "
        "you MUST call the calculate_math tool to compute the standard value, and you MUST store the returned result of the calculator tool call into the standard value field (e.g. K_value or a_value).\n"
        "CRITICAL: When calling calculate_math, formulate the mathematical expression using only raw numbers and mathematical functions (like log10, lg, ln, exp). "
        "Do NOT include variable names (such as 'c', 'K', 'a', 'v') in the expression. You must substitute the actual raw numerical value into the expression."
    )
    res_mh = ai.prompt(
        prompt=mh_prompt,
        schema=MarkHouwinkExtraction,
        tools=[calculate_math],
        system_instruction=mh_system_instruction
    )
    
    if res_mh.success:
        return TableInterpretationResponse(
            success=True,
            data=res_mh.data,
            usage_metadata=res_mh.usage_metadata,
            calculator_calls=res_mh.calculator_calls
        )
    else:
        return TableInterpretationResponse(
            success=False,
            error=res_mh.error,
            calculator_calls=res_mh.calculator_calls
        )
