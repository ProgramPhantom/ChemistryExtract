from pydantic import BaseModel, Field
from chemstractor.AI import AI
import pandas as pd
import os

class ColumnMapping(BaseModel):
    polymer_col: str | None = Field(
        None,
        description="The exact raw column name containing polymer names. Return null if no such column exists."
    )
    solvent_col: str | None = Field(
        None,
        description="The exact raw column name containing solvents. Return null if no such column exists."
    )
    diffusion_col: str | None = Field(
        None,
        description="The exact raw column name containing diffusion data (diffusion coefficient). Return null if no such column exists."
    )
    diffusion_multiplier: float = Field(
        1.0,
        description="The scientific multiplier found in the diffusion header (e.g., if header has 10^-8, return 1e-8. If none, return 1.0)."
    )
    diffusion_unit: str | None = Field(
        None,
        description="The clean standard unit of the diffusion coefficient found in the header, e.g., 'm^2/s' or 'cm^2/s'. Return null if not specified."
    )

class TableCleanResponse:
    success: bool
    error: str
    mapping: ColumnMapping | None
    usage_metadata: dict | None

    def __init__(self, success: bool, error: str = "", mapping: ColumnMapping | None = None, usage_metadata: dict | None = None):
        self.success = success
        self.error = error
        self.mapping = mapping
        self.usage_metadata = usage_metadata

def get_table_map(df: pd.DataFrame) -> TableCleanResponse:
    ai = AI.get_instance()
    
    # Send ONLY the headers and first two rows to save compute/tokens
    preview_csv = df.head(2).to_csv(index=False)
    
    prompt = f"""
    You are a chemical data mapping assistant. Look at this raw CSV snippet extracted from a PDF.
    Identify the exact column names for the polymer, solvent, and diffusion coefficient.
    Extract any scaling multiplier and clean unit from the diffusion column header.
    
    Raw Data:
    {preview_csv}
    """
    
    res = ai.prompt(
        prompt=prompt,
        schema=ColumnMapping,
    )
    
    if res.success:
        return TableCleanResponse(success=True, mapping=res.data, usage_metadata=res.usage_metadata)
    else:
        return TableCleanResponse(success=False, error=res.error)

def clean_csv(input_csv_path: str, output_csv_path: str) -> TableCleanResponse:
    # Load the raw data
    try:
        df = pd.read_csv(input_csv_path)
    except Exception as e:
        return TableCleanResponse(success=False, error=f"Failed to read CSV: {e}")
        
    res = get_table_map(df)
    if not res.success:
        return res
        
    mapping = res.mapping
    if not mapping.diffusion_col:
        return TableCleanResponse(success=False, error="No diffusion coefficient column identified by AI.", usage_metadata=res.usage_metadata)
        
    # Match raw columns to the Pydantic-provided names (handling case/whitespace variations)
    def find_exact_col(col_name):
        if not col_name:
            return None
        if col_name in df.columns:
            return col_name
        for c in df.columns:
            if str(c).strip().lower() == col_name.strip().lower():
                return c
        return None

    diff_col_exact = find_exact_col(mapping.diffusion_col)
    if not diff_col_exact:
        return TableCleanResponse(success=False, error=f"Diffusion column '{mapping.diffusion_col}' not found in CSV.", usage_metadata=res.usage_metadata)

    polymer_col_exact = find_exact_col(mapping.polymer_col)
    solvent_col_exact = find_exact_col(mapping.solvent_col)
    
    # Construct new DataFrame with clean headings
    new_df_data = {}
    
    # 1. Polymer
    if polymer_col_exact:
        new_df_data["Polymer"] = df[polymer_col_exact]
    else:
        new_df_data["Polymer"] = pd.Series([None] * len(df))
        
    # 2. Solvent
    if solvent_col_exact:
        new_df_data["Solvent"] = df[solvent_col_exact]
    else:
        new_df_data["Solvent"] = pd.Series([None] * len(df))
        
    # 3. Diffusion Coefficient
    multiplier_str = ""
    if mapping.diffusion_multiplier is not None:
        try:
            m_val = float(mapping.diffusion_multiplier)
            if m_val != 1.0:
                multiplier_str = f" x {mapping.diffusion_multiplier}"
        except ValueError:
            pass

    unit_str = f" ({mapping.diffusion_unit})" if mapping.diffusion_unit else ""
    diff_heading = f"Diffusion Coefficient{multiplier_str}{unit_str}"
    new_df_data[diff_heading] = df[diff_col_exact]
    
    clean_df = pd.DataFrame(new_df_data)
    
    # Save to new CSV
    try:
        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
        clean_df.to_csv(output_csv_path, index=False)
    except Exception as e:
        return TableCleanResponse(success=False, error=f"Failed to save clean CSV: {e}", usage_metadata=res.usage_metadata)
        
    return TableCleanResponse(success=True, mapping=mapping, usage_metadata=res.usage_metadata)
