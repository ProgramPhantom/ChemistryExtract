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

from processor import PDFProcessor
from main import AllSupportedModels

TEST_DIR = "./tests"
MATERIAL_DIR = "./tests/material"


def setup_run_layout(test_dir: str) -> tuple[str, str, str]:
    """Creates the timestamped directories for the run and returns their paths."""
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(test_dir, "runs", run_id)
    
    clean_dir = os.path.join(run_dir, "clean")
    output_dir = os.path.join(run_dir, "output")
    logs_dir = os.path.join(run_dir, "logs")
    
    os.makedirs(clean_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    return clean_dir, output_dir, logs_dir


def print_pdf_run_tree(
    console: Console,
    base_name: str,
    elapsed_time: float,
    clean_path: str,
    parsed_md_path: str,
    tables_dir: str,
    num_tables: int,
    log_file_path: str,
    categorise_tables: bool = False,
    summarise_tables: bool = False,
    model: str = "",
    cat_results: list = None,
    sum_results: list = None
):
    """Builds and prints the hierarchical tree status for a specific test run."""
    tree = Tree(f"[bold cyan]📄 {base_name}[/bold cyan] [dim](Completed in {elapsed_time:.2f}s)[/dim]")
    tree.add(f"[green]✓[/green] Extracted text & tables in-memory")
    tree.add(f"[green]✓[/green] Saved cleaned PDF to [yellow]{os.path.relpath(clean_path)}[/yellow]")
    tree.add(f"[green]✓[/green] Saved parsed markdown to [yellow]{os.path.relpath(parsed_md_path)}[/yellow]")
    tree.add(f"[green]✓[/green] Saved {num_tables} tables (txt & csv) to [yellow]{os.path.relpath(tables_dir)}[/yellow]")
    
    if categorise_tables:
        cat_node = tree.add(f"[green]✓[/green] Categorised extracted tables using [magenta]{model}[/magenta]")
        if not cat_results:
            cat_node.add("[dim]No tables found to categorise[/dim]")
        else:
            for table_name, success, status in cat_results:
                if success:
                    if "Does NOT contain" in status:
                        status_styled = f"[blue]{status}[/blue]"
                    else:
                        status_styled = f"[bold green]{status}[/bold green]"
                    cat_node.add(f"{table_name}: {status_styled}")
                else:
                    cat_node.add(f"{table_name}: [red]{status}[/red]")

    if summarise_tables:
        sum_node = tree.add(f"[green]✓[/green] Summarised experimental conditions using [magenta]{model}[/magenta]")
        if not sum_results:
            sum_node.add("[dim]No tables found to summarise[/dim]")
        else:
            for table_name, success, status in sum_results:
                if success:
                    sum_node.add(f"{table_name}: [bold green]{status}[/bold green]")
                else:
                    sum_node.add(f"{table_name}: [red]{status}[/red]")
                    
    tree.add(f"[green]✓[/green] Saved execution logs to [yellow]{os.path.relpath(log_file_path)}[/yellow]")
    
    console.print(tree)
    console.print()


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


def run_tests(categorise_tables: bool = True, summarise_tables: bool = True, model: AllSupportedModels = "gemini-2.5-flash"):
    # Initialize rich console targeting original stdout to bypass redirections
    console = Console(file=sys.__stdout__)
    
    # Find all test PDF files
    pdf_files = glob.glob(os.path.join(MATERIAL_DIR, "*.pdf"))
    
    console.print()
    console.print(Rule(title=f"[bold magenta]TESTING {len(pdf_files)} FILES[/bold magenta]", style="magenta"))
    console.print()
    
    # 1. Setup timestamped run directories
    clean_dir, output_dir, logs_dir = setup_run_layout(TEST_DIR)
    
    summary_data = []
    
    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path)
        base_no_ext = os.path.splitext(base_name)[0]
        
        # Configure output paths within the timestamped run directory
        test_output_dir = os.path.join(output_dir, base_no_ext)
        os.makedirs(test_output_dir, exist_ok=True)
        
        timer = time.time()
        
        # Initialize PDFProcessor
        processor = PDFProcessor(
            pdf_path=pdf_path,
            clean_dir=clean_dir,
            output_dir=test_output_dir,
            logs_dir=logs_dir,
            model=model
        )
        
        # Run standard PDF processing steps
        processor.extract(console)
        processor.save_cleaned_pdf()
        processor.save_outputs()
        
        if categorise_tables:
            processor.categorise_tables(console)
            
        if summarise_tables:
            processor.summarise_tables(console)
            
        if categorise_tables or summarise_tables:
            processor.create_excel()
            
        processor.save_logs()
        
        elapsed_time = time.time() - timer
        
        # Build and print tree list for this PDF file
        print_pdf_run_tree(
            console=console,
            base_name=processor.base_name,
            elapsed_time=elapsed_time,
            clean_path=processor.clean_path,
            parsed_md_path=processor.parsed_md_path,
            tables_dir=processor.tables_dir,
            num_tables=processor.num_tables,
            log_file_path=processor.log_file_path,
            categorise_tables=categorise_tables,
            summarise_tables=summarise_tables,
            model=model,
            cat_results=processor.cat_results,
            sum_results=processor.sum_results
        )
        
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
    run_tests(model="gemini", categorise_tables=True, summarise_tables=True)