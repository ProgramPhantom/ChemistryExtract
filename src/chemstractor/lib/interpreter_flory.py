import math
from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, Field
from chemstractor.AI import AI


# Define the schema for a SINGLE equation/row (Flory)
class FloryEntry(BaseModel):
    polymer_name: str = Field(description="The name or acronym of the polymer. If missing or omitted in the table, set to 'Not found'.")
    solvent: str = Field(description="The solvent used. If missing or omitted in the table, set to 'Not found'.")
    temperature_k: Optional[float | str] = Field(None, description="Temperature in Kelvin, if stated in the text or table. If missing or omitted in the table, set to 'Not found'.")
    
    raw_v_value: float | str = Field(description="The raw value representing the Flory scaling exponent / molar mass dependency parameter (often represented as v, nu, a, b, or alpha in different equation forms). Do not include any uncertainty/ranges (like ±0.02) in this number. If missing or omitted in the table, set to 'Not found'.")
    v_transformation: str = Field(description="Transformation applied to v (optional). E.g. 'none', 'log', 'ln', or any custom scaling expression.")
    v_value: float | str = Field(description="The standard, calculated/converted value of the coefficient v. If v is scaled or transformed in the table, you MUST call the calculate_math tool to compute the standard value and store that returned result here. If no transformation is applied, v_value = raw_v_value. If v is missing or omitted in the table, set to 'Not found'.")
    
    raw_c_value: float | str = Field(description="The raw value of the constant representing the Flory constant / pre-exponential factor (often represented as c, C, b', K, or A in different equation forms) as written in the table, before log conversion or error correction. Do not include any uncertainty/ranges (like ±0.02) in this number. If missing or omitted in the table, set to 'Not found'.")
    c_transformation: str = Field(description="Transformation applied to c (optional). E.g. 'none', 'log', 'ln', or any custom scaling/exponent expression.")
    c_value: float | str = Field(description="The log-form (base-10 logarithm) value of the Flory constant. If the constant in the table is already in log form (e.g. under a log(b') or lg(c) header), store the corrected log value here (fixing omitted minus signs if any). If the constant is in linear form, convert it to its base-10 log value and store that here. If c is missing or omitted in the table, set to 'Not found'.")


# Define the extraction schema for flory parameters
class FloryExtraction(BaseModel):
    is_flory_data: bool = Field(
        description="True if the table contains Flory coefficient or constant parameters (v or c, or both). False otherwise."
    )
    flory_entries: List[FloryEntry] = Field(
        default=[],
        description="A list containing one entry for EVERY valid Flory parameter row in the table. Do not skip any rows."
    )


class TableInterpretationResponse:
    success: bool
    error: str
    data: FloryExtraction | None
    usage_metadata: dict | None
    calculator_calls: List[dict]

    def __init__(self, success: bool, error: str = "", data: FloryExtraction | None = None, usage_metadata: dict | None = None, calculator_calls: List[dict] = None):
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


def get_flory_interpret_prompt(table_text: str, title: str | None = None, abstract: str | None = None, formulae: List[str] | None = None) -> str:
    context_str = ""
    if title:
        context_str += f"\n    Paper Title: {title}"
    if abstract:
        context_str += f"\n    Paper Abstract: {abstract}"
    if formulae:
        context_str += "\n    Extracted Mathematical Formulae:\n" + "\n".join(f"    - {formula}" for formula in formulae)
        
    return f"""
    You are an expert chemistry data converter and reasoning engine. Your task is to analyze the following table and its surrounding context, deduce which columns represent the polymer diffusion scaling parameters, and extract them.

    ### Chemical & Physical Context:
    We are looking for polymer/solvent diffusion calibration parameters. In physical chemistry, the diffusion coefficient (D) of a polymer depends on its molecular weight (or molar mass, M) according to a scaling relationship (power-law):
    
    D = A * M^(-v)
    
    where:
    - "v" (or nu, alpha, a, b, V, or a_D) is the Flory coefficient / scaling exponent representing the Molar Mass Dependency. It typically lies between 0.33 (spherical particles/highly branched) and 1.0 (rigid rods), and is most commonly around 0.40 to 0.60 for linear polymers in solution.
    - The pre-exponential factor (e.g., A, c, b', K, or D_0) is the Flory constant. It represents the intercept of the relation in logarithmic space:
      log(D) = log(b') - v * log(M). CRITICAL: Please be aware that the equation above has the minus sign built in, meaning we ALWAYS
      expect the v value to be positive. Make sure the v value you return is always positive by making the appropriate transformation.
    
    ### Deduction & Extraction Guidelines:
    1. **Analyze Context & Formulas**: Look at the Paper Title, Abstract, and Extracted Mathematical Formulae. Identify the specific equation form used by the authors for diffusion calibration (e.g., whether they use uncorrected constants like b' or viscosity-corrected constants like c).
    2. **Deduce Column Meanings**:
       - Do not strictly look for columns named exactly "c" or "v". Instead, use chemical reasoning to map the columns based on the equation's role.
       - **Exponent Column (Molar Mass Dependency 'v')**: Identify the column representing the exponent or slope. Look for headers like `v`, `V`, `nu`, `a`, `b`, `alpha`, `exponent`, or `slope`. The values are typically dimensionless and lie in the range 0.35 to 0.70.
       - **Constant Column (Flory Constant 'c')**: Identify the column representing the pre-exponential factor or intercept. Look for headers like `lg(c...)`, `lg(b'...)`, `log(c)`, `log(b')`, `c`, `b'`, `K`, or `A`. If the table contains both uncorrected (e.g., b') and viscosity-corrected (e.g., c) constants, extract the UNCORRECTED constant (representing b' or similar).
    3. **Uncertainty/Range Handling**: If a cell contains a value with uncertainty (e.g., "7.94 ± 0.02" or "0.49 ± 0.02"), extract ONLY the nominal/base value (e.g., "7.94" or "0.49") as the raw value. Do not include the uncertainty symbol or the range.
    4. **Transformation & Calculations to Log Form**:
       - We require the final output `c_value` to be in **log form (base-10 logarithm)** for log-log plotting.
       - **If the constant column is already in log form** (e.g. `lg(b')`, `lg(c)`, `log(b')`, or `log(c)`): Leave the value in its log form (e.g., -7.70). Do NOT exponentiate it back to linear form.
       - **If the constant column is in linear/normal form** (e.g. `c` or `b'`): Convert the linear value to its base-10 log form.
    5. **Sanity Check & Error Correction (Omitted Minus Signs)**:
       - Since the table text is parsed from PDFs, characters (especially minus signs `-`) are sometimes omitted or corrupted during parsing.
       - The log of the polymer diffusion constant (e.g., log10(b') or log10(c)) is expected to be a negative number, typically between `-8` and `-7` (for diffusion in standard SI units m^2/s).
       - If you read a positive constant value (e.g., `7.70`, `8`, or `7.94`) under a log-constant column (like `lg(b')`), this is clearly a parsing error where the minus sign was omitted. You **MUST** correct this by adding a minus sign (e.g. `7.70` becomes `-7.70`, `7.94` becomes `-7.94`).
       - Similarly, we expect the returned v value to ALWAYS be positive. Sometimes the diffusion equation being used may not have -v built in, so be aware of this.
    6. **Missing Data & Partial Flory Entries**:
       - Sometimes only part of the Flory data structure is present in a table (for example, the exponent `v` value is present but the constant `c` value is missing, or vice-versa).
       - If any specific field or parameter of `FloryEntry` is missing or not present in the table, set that field's value to `"Not found"`.
       - CRITICAL: Do NOT hallucinate, guess, or fabricate missing values or constants if they are not explicitly present in the table.

    {context_str}
    
    Table Data:
    {table_text}
    """


def interpret_flory_table(table_text: str, title: str | None = None, abstract: str | None = None, formulae: List[str] | None = None) -> TableInterpretationResponse:
    ai = AI.get_instance()
    
    flory_prompt = get_flory_interpret_prompt(table_text, title=title, abstract=abstract, formulae=formulae)
    flory_system_instruction = (
        "You are a precise chemistry data extractor. You must NEVER do math in your head. "
        "For the exponent/v value, if it is scaled or transformed, you MUST call calculate_math to compute the standard value. "
        "For the constant/c value, we require it in log form (base-10 logarithm). If the constant is already in log form (e.g. lg(b') or log(c)), keep it as is (fixing any omitted minus signs so it is negative, e.g. 7.70 becomes -7.70). "
        "If the constant is in linear/normal form, convert it to its base-10 log form. "
        "CRITICAL: If any part of the FloryEntry data structure is missing or not present in the table (e.g. the v value is present but the c value is missing, or vice versa), set that missing field to 'Not found'. You MUST respond with 'Not found' if a certain part of the FloryEntry data structure is missing in the table. Do NOT hallucinate or guess missing values. "
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
        return TableInterpretationResponse(
            success=True,
            data=res_flory.data,
            usage_metadata=res_flory.usage_metadata,
            calculator_calls=res_flory.calculator_calls
        )
    else:
        return TableInterpretationResponse(
            success=False,
            error=res_flory.error,
            calculator_calls=res_flory.calculator_calls
        )
