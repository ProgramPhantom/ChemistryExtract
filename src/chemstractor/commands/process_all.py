import os
import sys
import glob
import time
from datetime import datetime
from rich.console import Console
from rich.rule import Rule
from rich.table import Table

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
    direct: bool = False
):
    console = Console(file=sys.__stdout__)
    
    # Use the middleware helper to resolve directories and prepare extracts
    from chemstractor.commands.utils import prepare_batch_dirs
    pdf_dir, run_dir, items = prepare_batch_dirs(pdf_dir, output_parent_dir, direct=direct)
    
    console.print()
    label = "ANALYSING" if direct else "PROCESSING"
    console.print(Rule(title=f"[bold magenta]{label} {len(items)} ITEMS[/bold magenta]", style="magenta"))
    console.print()
    
    summary_data = []
    
    if direct:
        for dest_subdir_path in items:
            res = run_process_single(
                pdf_path=dest_subdir_path,
                output_dir=dest_subdir_path,
                console=console,
                direct=True,
                same_folder=True
            )
            summary_data.append(res)
    else:
        for pdf_path in items:
            res = run_process_single(
                pdf_path=pdf_path,
                output_dir=run_dir,
                console=console,
                direct=False
            )
            summary_data.append(res)
            
    # Print the final summary table
    print_summary_table(console, summary_data)
    