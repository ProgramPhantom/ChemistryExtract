import sys
## Allows unicode in std out
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import glob
import os
import time
from datetime import datetime

from rich.console import Console
from rich.tree import Tree
from rich.rule import Rule
from rich.table import Table
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels
from chemstractor.commands.extract import run_extract
from chemstractor.commands.categorise import run_categorise
from chemstractor.commands.summarise import run_summarise

TEST_DIR = "./tests"
MATERIAL_DIR = "./tests/material"


def setup_run_layout(test_dir: str) -> str:
    """Creates the timestamped directories for the run and returns its path."""
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(test_dir, "runs", run_id)
    os.makedirs(run_dir, exist_ok=True)
    return run_dir


def print_summary_table(console: Console, summary_data: list[dict]):
    """Prints the final summary table of all PDF runs."""
    console.print(Rule(title="[bold green]TEST SUITE SUMMARY[/bold green]", style="green"))
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


def test_all_command(categorise_tables: bool = True, summarise_tables: bool = True, model: AllSupportedModels = "gemini-2.5-flash"):
    # Initialize rich console targeting original stdout to bypass redirections
    console = Console(file=sys.__stdout__)
    
    # Scan for PDF files in the material directory
    pdf_pattern = os.path.join(MATERIAL_DIR, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        console.print(f"[bold red]Error: No PDF files found in {MATERIAL_DIR}[/bold red]")
        return
        
    console.print()
    console.print(Rule(title=f"[bold magenta]TESTING {len(pdf_files)} FILES[/bold magenta]", style="magenta"))
    console.print()
    
    # 1. Setup timestamped run directories
    run_dir = setup_run_layout(TEST_DIR)
    
    summary_data = []
    
    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path)
        base_no_ext = os.path.splitext(base_name)[0]
        
        # Configure output paths within the timestamped run directory
        test_output_dir = os.path.join(run_dir, base_no_ext)
        os.makedirs(test_output_dir, exist_ok=True)
        
        timer = time.time()
        
        # Initialize PDFProcessor
        processor = PDFProcessor(
            pdf_path=pdf_path,
            output_dir=test_output_dir,
            model=model
        )
        
        tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
        
        with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
            # 1. Extract
            run_extract(processor, tree)
            
            # 2. Categorise
            if categorise_tables:
                run_categorise(processor, tree)
                
            # 3. Summarise
            if summarise_tables:
                run_summarise(processor, tree)
                
            processor.save()
            live.refresh()
            
        elapsed_time = time.time() - timer
        
        # Collect data for final summary table
        summary_data.append({
            "file": processor.base_name,
            "tables": processor.num_tables,
            "time": elapsed_time
        })

        # Deload extractor instance to release memory
        processor.cleanup()
        
    # Print the final summary table
    print_summary_table(console, summary_data)


if __name__ == "__main__":    
    test_all_command(model="gemini", categorise_tables=True, summarise_tables=True)