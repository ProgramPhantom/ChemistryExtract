import os
import sys
import glob
import time
from datetime import datetime
from rich.console import Console
from rich.rule import Rule
from rich.table import Table

from chemstractor.models import AllSupportedModels
from chemstractor.commands.process import run_process_single

def setup_run_layout(output_parent_dir: str) -> str:
    """Creates the timestamped directories for the run and returns its path."""
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(output_parent_dir, run_id)
    os.makedirs(run_dir, exist_ok=True)
    return run_dir

def print_summary_table(console: Console, summary_data: list[dict]):
    """Prints the final summary table of all PDF runs."""
    console.print(Rule(title="[bold green]PROCESS ALL SUMMARY[/bold green]", style="green"))
    console.print()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("PDF File", style="cyan")
    table.add_column("Tables Extracted", justify="right", style="green")
    table.add_column("Execution Time", justify="right", style="yellow")
    
    total_time = 0.0
    total_tables = 0
    for row in summary_data:
        table.add_row(
            row["file"],
            str(row["tables"]),
            f"{row['time']:.2f}s"
        )
        total_time += row["time"]
        total_tables += row["tables"]
        
    table.add_section()
    table.add_row(
        "[bold]Total[/bold]",
        f"[bold]{total_tables}[/bold]",
        f"[bold]{total_time:.2f}s[/bold]"
    )
    console.print(table)
    console.print()

def process_all_command(
    pdf_dir: str,
    output_parent_dir: str,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash"
):
    console = Console(file=sys.__stdout__)
    
    # Scan for PDF files in the material directory
    pdf_pattern = os.path.join(pdf_dir, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        console.print(f"[bold red]Error: No PDF files found in {pdf_dir}[/bold red]")
        return
        
    console.print()
    console.print(Rule(title=f"[bold magenta]PROCESSING {len(pdf_files)} FILES[/bold magenta]", style="magenta"))
    console.print()
    
    # 1. Setup timestamped run directory
    run_dir = setup_run_layout(output_parent_dir)
    
    summary_data = []
    
    for pdf_path in pdf_files:
        res = run_process_single(
            pdf_path=pdf_path,
            output_dir=run_dir,
            categorise_tables=categorise_tables,
            summarise_tables=summarise_tables,
            model=model,
            console=console
        )
        summary_data.append(res)
        
    # Print the final summary table
    print_summary_table(console, summary_data)
    
    # Run validation on the generated outputs if validation directory exists
    validation_dir = "./tests/validation"
    if not os.path.exists(validation_dir):
        validation_dir = "tests/validation"
    if os.path.exists(validation_dir):
        from chemstractor.commands.validate import validate_command
        validate_command(run_dir, validation_dir)
