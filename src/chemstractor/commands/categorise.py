import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels, pricing_matrix

def categorise_command(pdf_path: str, clean_dir: str, output_dir: str, logs_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
    console = Console(file=sys.__stdout__)
    base_name = os.path.basename(pdf_path)
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(clean_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    tree = Tree(f"[bold cyan]📄 {base_name}[/bold cyan]")
    
    processor = PDFProcessor(
        pdf_path=pdf_path,
        clean_dir=clean_dir,
        output_dir=output_dir,
        logs_dir=logs_dir,
        model=model
    )
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        # Step 1: Extract
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
        
        # Step 2: Categorise
        cat_node = tree.add(Spinner("dots", text="[bold cyan]Categorising extracted tables...[/bold cyan]"))
        for event in processor.categorise_generator():
            if event["status"] == "working" or event["status"] == "table_start":
                cat_node.label = f"[bold cyan]{event['message']}[/bold cyan]"
            elif event["status"] == "complete":
                elapsed_time = event["elapsed_time"]
                cat_results = event["results"]
                
                # Compute token counts/costs
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
                        table_name, success, status, usage_metadata = item
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
                            if "Does NOT contain" in status:
                                status_styled = f"[blue]{status}[/blue]"
                            else:
                                status_styled = f"[bold green]{status}[/bold green]"
                            cat_node.add(f"{table_name}: {status_styled}{tokens_str}")
                        else:
                            cat_node.add(f"{table_name}: [red]{status}[/red]")
        
        processor.create_excel()
        live.refresh()
        
    processor.cleanup()
