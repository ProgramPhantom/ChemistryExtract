import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels, pricing_matrix
from chemstractor.commands.extract import run_extract

def run_categorise(processor: PDFProcessor, tree: Tree):
    """Executes the categorisation process on the processor and updates the rich Tree with status/pricing."""
    cat_node = tree.add(Spinner("dots", text="[bold cyan]Categorising extracted tables...[/bold cyan]"))
    model = processor.model
    for event in processor.categorise():
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

def categorise_command(pdf_path: str, output_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
    console = Console(file=sys.__stdout__)
    base_name = os.path.basename(pdf_path)
    
    tree = Tree(f"[bold cyan]📄 {base_name}[/bold cyan]")
    
    processor = PDFProcessor(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=model
    )
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        run_extract(processor, tree)
        run_categorise(processor, tree)
        processor.save()
        live.refresh()
        
    processor.cleanup()
