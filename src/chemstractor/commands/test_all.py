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
from rich.spinner import Spinner

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels, pricing_matrix

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
        
        tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
        
        with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
            # 1. Extract
            ext_node = tree.add(Spinner("dots", text="[bold cyan]Extracting text & tables...[/bold cyan]"))
            for event in processor.extract_generator():
                if event["status"] == "complete":
                    elapsed_time = event["elapsed_time"]
                    num_tables = event["num_tables"]
                    ext_node.label = f"[green]✓[/green] Extracted text & tables [dim](completed in {elapsed_time:.2f}s)[/dim]"
                    ext_node.add("Extracted text & tables in-memory")
                    ext_node.add(f"Saved cleaned PDF to [yellow]{os.path.relpath(processor.clean_path)}[/yellow]")
                    ext_node.add(f"Saved parsed markdown to [yellow]{os.path.relpath(processor.parsed_md_path)}[/yellow]")
                    ext_node.add(f"Saved {num_tables} tables (txt & csv) to [yellow]{os.path.relpath(processor.tables_dir)}[/yellow]")
                    ext_node.add(f"Saved execution logs to [yellow]{os.path.relpath(processor.log_file_path)}[/yellow]")
            
            # 2. Categorise
            if categorise_tables:
                cat_node = tree.add(Spinner("dots", text="[bold cyan]Categorising extracted tables...[/bold cyan]"))
                for event in processor.categorise_generator():
                    if event["status"] == "working" or event["status"] == "table_start":
                        cat_node.label = f"[bold cyan]{event['message']}[/bold cyan]"
                    elif event["status"] == "complete":
                        elapsed_time = event["elapsed_time"]
                        cat_results = event["results"]
                        
                        total_in = 0
                        total_out = 0
                        has_tokens = False
                        for item in cat_results:
                            if len(item) == 4 and item[3]:
                                total_in += item[3].get("prompt_token_count", 0)
                                total_out += item[3].get("candidates_token_count", 0)
                                has_tokens = True
                                
                        tokens_title = ""
                        if has_tokens:
                            cost_str = ""
                            if model in pricing_matrix:
                                pricing = pricing_matrix[model]
                                cost = (total_in * pricing["input_per_m"] + total_out * pricing["output_per_m"]) / 1_000_000
                                cost_str = f"; Cost: ${cost:.6f}"
                            tokens_title = f" (Total tokens: {total_in} in, {total_out} out{cost_str})"
                            
                        cat_node.label = f"[green]✓[/green] Categorised extracted tables using [magenta]{model}[/magenta] [dim](completed in {elapsed_time:.2f}s){tokens_title}[/dim]"
                        
                        if not cat_results:
                            cat_node.add("[dim]No tables found to categorise[/dim]")
                        else:
                            for item in cat_results:
                                table_name, success, status_val, usage_metadata = item
                                tokens_str = ""
                                if usage_metadata:
                                    in_t = usage_metadata.get("prompt_token_count", 0)
                                    out_t = usage_metadata.get("candidates_token_count", 0)
                                    cost_item_str = ""
                                    if model in pricing_matrix:
                                        pricing = pricing_matrix[model]
                                        cost_item = (in_t * pricing["input_per_m"] + out_t * pricing["output_per_m"]) / 1_000_000
                                        cost_item_str = f"; Cost: ${cost_item:.6f}"
                                    tokens_str = f" [dim](tokens: {in_t} in, {out_t} out{cost_item_str})[/dim]"
                                    
                                if success:
                                    if "Does NOT contain" in status_val:
                                        status_styled = f"[blue]{status_val}[/blue]"
                                    else:
                                        status_styled = f"[bold green]{status_val}[/bold green]"
                                    cat_node.add(f"{table_name}: {status_styled}{tokens_str}")
                                else:
                                    cat_node.add(f"{table_name}: [red]{status_val}[/red]")
                                    
            # 3. Summarise
            if summarise_tables:
                sum_node = tree.add(Spinner("dots", text="[bold cyan]Summarising experimental conditions...[/bold cyan]"))
                for event in processor.summarise_generator():
                    if event["status"] == "working" or event["status"] == "table_start":
                        sum_node.label = f"[bold cyan]{event['message']}[/bold cyan]"
                    elif event["status"] == "complete":
                        elapsed_time = event["elapsed_time"]
                        sum_results = event["results"]
                        metadata_res = processor.metadata_res
                        
                        total_in = 0
                        total_out = 0
                        has_tokens = False
                        if metadata_res and metadata_res.success and metadata_res.usage_metadata:
                            total_in += metadata_res.usage_metadata.get("prompt_token_count", 0)
                            total_out += metadata_res.usage_metadata.get("candidates_token_count", 0)
                            has_tokens = True
                        for item in sum_results:
                            if len(item) == 4 and item[3]:
                                total_in += item[3].get("prompt_token_count", 0)
                                total_out += item[3].get("candidates_token_count", 0)
                                has_tokens = True
                                
                        tokens_title = ""
                        if has_tokens:
                            cost_str = ""
                            if model in pricing_matrix:
                                pricing = pricing_matrix[model]
                                cost = (total_in * pricing["input_per_m"] + total_out * pricing["output_per_m"]) / 1_000_000
                                cost_str = f"; Cost: ${cost:.6f}"
                            tokens_title = f" (Total tokens: {total_in} in, {total_out} out{cost_str})"
                            
                        sum_node.label = f"[green]✓[/green] Summarised experimental conditions using [magenta]{model}[/magenta] [dim](completed in {elapsed_time:.2f}s){tokens_title}[/dim]"
                        
                        if metadata_res:
                            tokens_str = ""
                            if metadata_res.usage_metadata:
                                in_t = metadata_res.usage_metadata.get("prompt_token_count", 0)
                                out_t = metadata_res.usage_metadata.get("candidates_token_count", 0)
                                cost_item_str = ""
                                if model in pricing_matrix:
                                    pricing = pricing_matrix[model]
                                    cost_item = (in_t * pricing["input_per_m"] + out_t * pricing["output_per_m"]) / 1_000_000
                                    cost_item_str = f"; Cost: ${cost_item:.6f}"
                                tokens_str = f" [dim](tokens: {in_t} in, {out_t} out{cost_item_str})[/dim]"
                                
                            if metadata_res.success:
                                sum_node.add(f"Paper Metadata: [bold green]Successfully extracted[/bold green]{tokens_str}")
                            else:
                                sum_node.add(f"Paper Metadata: [red]Failed: {metadata_res.error}[/red]")
                                
                        if not sum_results:
                            sum_node.add("[dim]No tables found to summarise[/dim]")
                        else:
                            for item in sum_results:
                                table_name, success, status_val, usage_metadata = item
                                tokens_str = ""
                                if usage_metadata:
                                    in_t = usage_metadata.get("prompt_token_count", 0)
                                    out_t = usage_metadata.get("candidates_token_count", 0)
                                    cost_item_str = ""
                                    if model in pricing_matrix:
                                        pricing = pricing_matrix[model]
                                        cost_item = (in_t * pricing["input_per_m"] + out_t * pricing["output_per_m"]) / 1_000_000
                                        cost_item_str = f"; Cost: ${cost_item:.6f}"
                                    tokens_str = f" [dim](tokens: {in_t} in, {out_t} out{cost_item_str})[/dim]"
                                    
                                if success:
                                    sum_node.add(f"{table_name}: [bold green]{status_val}[/bold green]{tokens_str}")
                                else:
                                    sum_node.add(f"{table_name}: [red]{status_val}[/red]")
                                    
            if categorise_tables or summarise_tables:
                processor.create_excel()
            
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