import math
from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, Field
from chemstractor.AI import AI


# 1. Define the schema for a SINGLE equation/row (Mark-Houwink)
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


# 2. Define the schema for a SINGLE equation/row (Flory)
class FloryEntry(BaseModel):
    polymer_name: str = Field(description="The name or acronym of the polymer.")
    solvent: str = Field(description="The solvent used.")
    temperature_k: Optional[float] = Field(None, description="Temperature in Kelvin, if stated in the text or table.")
    raw_v_value: float = Field(description="The raw number representing the Flory coefficient/exponent v (often represented as nu or v).")
    v_transformation: str = Field(description="Transformation applied to v. E.g. 'none', 'reciprocal', 'unknown', or any custom scaling expression.")
    v_value: float = Field(description="The standard, calculated/converted value of the coefficient v. If v is scaled or transformed in the table, you MUST call the calculate_math tool to compute the standard value and store that returned result here. If no transformation is applied, v_value = raw_v_value.")
    raw_c_value: float = Field(description="The raw number representing the Flory constant c (often represented as C or c).")
    c_transformation: str = Field(description="Transformation applied to c. E.g. 'none', 'log', 'ln', '10**-8', 'unknown', or any custom multiplier/scaling expression.")
    c_value: float = Field(description="The standard, calculated/converted value of the constant c. If c is scaled or transformed in the table (e.g. log, ln, or multiplied by a factor of 10), you MUST call the calculate_math tool to compute the standard value and store that returned result here. If no transformation is applied, c_value = raw_c_value.")


# 3. Define the extraction schema for Mark-Houwink parameters
class MarkHouwinkExtraction(BaseModel):
    is_mark_houwink_data: bool = Field(
        description="True if the table contains Mark-Houwink equation parameters (K and a). False otherwise."
    )
    mh_entries: List[MarkHouwinkEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Mark-Houwink row in the table. Do not skip any rows."
    )


# 4. Define the extraction schema for flory parameters
class FloryExtraction(BaseModel):
    is_flory_data: bool = Field(
        description="True if the table contains Flory coefficient and constant parameters (v and c). False otherwise."
    )
    flory_entries: List[FloryEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Flory parameter row in the table. Do not skip any rows."
    )


# 5. Class containing combined extraction data.
class TableExtraction(BaseModel):
    is_mark_houwink_data: bool = Field(
        description="True if the table contains Mark-Houwink equation parameters (K and a, or equivalent notation). False otherwise."
    )
    is_flory_data: bool = Field(
        description="True if the table contains Flory coefficient and constant parameters (v and c, or equivalent notation). False otherwise."
    )
    mh_entries: List[MarkHouwinkEntry] = Field(
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


def get_flory_interpret_prompt(table_text: str, title: str | None = None, abstract: str | None = None, formulae: List[str] | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"
    if formulae:
        context_str += "\n    Extracted Mathematical Formulae:\n" + "\n".join(f"    - {formula}" for formula in formulae)
        
    return f"""
    You are a chemistry data converter. Analyze the following extracted table and its surrounding context.
    Your task is to extract Flory parameters (coefficient v and constant c) for each row where applicable.
    
    CRITICAL: Try to find a formula of the form "D = cM^{{-v}}" (or equivalent notation) in the paper text/context to determine the meaning of the column titles and to correctly select the constant c and Flory coefficient v.
    
    For Flory entries:
    Extract the polymer name, solvent, temperature, and Flory parameters (coefficient v and constant c).
    
    If the coefficient v or constant c in the table are transformed (for example, if they are listed as log(c), ln(c), 1/v, or reciprocal of v),
    you MUST call the `calculate_math` tool to compute the standard/converted v and c values.
    Do NOT do any math, logarithm, exponentiation, or reciprocal calculation in your head. Use the `calculate_math` tool!
    
    {context_str}
    
    Table Data:
    {table_text}
    """


def interpret_table(table_text: str, title: str | None = None, abstract: str | None = None, cat_data: dict | None = None, formulae: List[str] | None = None) -> TableInterpretationResponse:
    ai = AI.get_instance()
    
    # 1. Determine targets based on cat_data
    extract_mh = False
    extract_flory = False
    if cat_data:
        if cat_data.get("contains_mark_houwink_parameters", False):
            extract_mh = True
        if cat_data.get("contains_flory_parameters", False):
            extract_flory = True
            
    # Fallback if neither is specified
    if not extract_mh and not extract_flory:
        extract_mh = True
        extract_flory = True
        
    mh_res = None
    flory_res = None
    all_calculator_calls = []
    total_usage_metadata = {
        "prompt_token_count": 0,
        "candidates_token_count": 0,
        "total_token_count": 0
    }
    
    # 2. Extract Mark-Houwink parameters
    if extract_mh:
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
            mh_res = res_mh.data
            if res_mh.calculator_calls:
                all_calculator_calls.extend(res_mh.calculator_calls)
            if res_mh.usage_metadata:
                for k, v in res_mh.usage_metadata.items():
                    if k in total_usage_metadata:
                        total_usage_metadata[k] += v
        else:
            return TableInterpretationResponse(
                success=False,
                error=f"Mark-Houwink extraction failed: {res_mh.error}",
                calculator_calls=res_mh.calculator_calls
            )
            
    # 3. Extract Flory parameters
    if extract_flory:
        flory_prompt = get_flory_interpret_prompt(table_text, title=title, abstract=abstract, formulae=formulae)
        flory_system_instruction = (
            "You are a precise chemistry data extractor. You must NEVER do math in your head. "
            "If any parameter is transformed or scaled in the table (e.g. log, ln, reciprocal, or a power of 10 multiplier like 10^-8), "
            "you MUST call the calculate_math tool to compute the standard value, and you MUST store the returned result of the calculator tool call into the standard value field (e.g. v_value or c_value).\n"
            "CRITICAL: When calling calculate_math, formulate the mathematical expression using only raw numbers and mathematical functions (like log10, lg, ln, exp). "
            "Do NOT include variable names (such as 'c', 'K', 'a', 'v') in the expression. You must substitute the actual raw numerical value into the expression."
        )
        res_flory = ai.prompt(
            prompt=flory_prompt,
            schema=FloryExtraction,
            tools=[calculate_math],
            system_instruction=flory_system_instruction
        )
        if res_flory.success:
            flory_res = res_flory.data
            if res_flory.calculator_calls:
                all_calculator_calls.extend(res_flory.calculator_calls)
            if res_flory.usage_metadata:
                for k, v in res_flory.usage_metadata.items():
                    if k in total_usage_metadata:
                        total_usage_metadata[k] += v
        else:
            return TableInterpretationResponse(
                success=False,
                error=f"Flory extraction failed: {res_flory.error}",
                calculator_calls=all_calculator_calls + (res_flory.calculator_calls or [])
            )
            
    # 4. Merge results into TableExtraction
    is_mh = mh_res.is_mark_houwink_data if mh_res else False
    is_fl = flory_res.is_flory_data if flory_res else False
    mh_entries = mh_res.mh_entries if mh_res else []
    flory_entries = flory_res.flory_entries if flory_res else []
    
    merged_data = TableExtraction(
        is_mark_houwink_data=is_mh,
        is_flory_data=is_fl,
        mh_entries=mh_entries,
        flory_entries=flory_entries
    )
    
    return TableInterpretationResponse(
        success=True,
        data=merged_data,
        usage_metadata=total_usage_metadata,
        calculator_calls=all_calculator_calls
    )
