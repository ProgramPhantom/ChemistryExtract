from pydantic import BaseModel, Field
from chemstractor.AI import AI

class ExtraStatistic(BaseModel):
    name: str = Field(description="The name of the variable, parameter, or statistic (e.g. 'pH', 'concentration', 'density').")
    value: str = Field(description="The value of this parameter/statistic.")

class ExperimentalConditions(BaseModel):
    description: str = Field(
        description="A paragraph describing the experimental conditions under which the data in the table was gathered. Use 'Not applicable' if the table does not present experimental data or the context does not specify conditions."
    )
    temperature: str | None = Field(
        None,
        description="The temperature(s) at which the experiment was conducted (e.g. '298.15 K', '25 °C'), or 'Not applicable' if not experimental data or 'Not found' if not specified"
    )
    pressure: str | None = Field(
        None,
        description="The pressure(s) at which the experiment was conducted (e.g. '1 atm', '101.3 kPa'), or 'Not applicable' if not experimental data or 'Not found' if not specified"
    )
    chemicals: list[str] = Field(
        default_factory=list,
        description="The list of chemicals or substances involved in the experiment or table (e.g. reagents, solvents, reactants, products), or an empty list if not applicable or none specified."
    )
    other_statistics: list[ExtraStatistic] = Field(
        default_factory=list,
        description="Other key experimental variables, parameters, or statistics found in the table or context (e.g. pH, concentration, density, activation energy) represented as list of key-value objects. If none are found or if not applicable, return an empty list."
    )

class TableSummaryResponse:
    success: bool
    error: str
    data: ExperimentalConditions | None
    usage_metadata: dict | None

    def __init__(self, success: bool, error: str, data: ExperimentalConditions | None = None, usage_metadata: dict | None = None):
        self.success = success
        self.error = error
        self.data = data
        self.usage_metadata = usage_metadata


def get_summarise_prompt(table_summary: str) -> str:
    return f"""
    You are a chemistry data extraction assistant. Analyze the following extracted table and its surrounding context,
    and extract/summarize the experimental conditions.
    
    If the table does not represent experimental data or does not contain experimental conditions, set the fields (description, temperature, pressure) to "Not applicable" and return an empty list for chemicals and other_statistics.
    
    Table Summary:
    {table_summary}
    """


def summarise_table_conditions(table_summary: str) -> TableSummaryResponse:
    ai = AI.get_instance()
    prompt = get_summarise_prompt(table_summary)
    
    res = ai.prompt(
        prompt=prompt,
        schema=ExperimentalConditions,
    )
    
    if res.success:
        return TableSummaryResponse(success=True, error="", data=res.data, usage_metadata=res.usage_metadata)
    else:
        return TableSummaryResponse(success=False, error=res.error)
