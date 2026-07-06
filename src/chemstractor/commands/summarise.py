import sys
import os
import time
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.commands.extract import run_extract
from chemstractor.AI import AI, pricing_matrix

def run_summarise(processor: PDFProcessor, tree: Tree):
    """Executes the summarisation process on the processor and updates the rich Tree with status/pricing."""

    sum_node = tree.add(Spinner("dots", text="[bold cyan]Summarising experimental conditions...[/bold cyan]"))
    model = AI.get_instance().selected_model

    for event in processor.summarise():

        if event["status"] == "working" or event["status"] == "table_start":
            sum_node.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
            
        elif event["status"] == "complete":
            elapsed_time = event["elapsed_time"]
            sum_results = event["results"]
            
            # Compute token counts/costs
            total_in = 0
            total_out = 0
            has_tokens = False
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
            
            if not sum_results:
                sum_node.add("[dim]No tables found to summarise[/dim]")
            else:
                for item in sum_results:
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
                        sum_node.add(f"{table_name}: [bold green]{status}[/bold green]{tokens_str}")
                    else:
                        sum_node.add(f"{table_name}: [red]{status}[/red]")


def summarise_command(
    pdf_path: str,
    output_dir: str,
    direct: bool = False,
    same_folder: bool = True
):
    console = Console(file=sys.__stdout__)
    
    # Initialize PDFProcessor using prepare_processor middleware
    from chemstractor.commands.utils import prepare_processor
    processor, output_dir = prepare_processor(
        pdf_path_or_dir=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder,
        suffix="summarised"
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    from chemstractor.commands.metadata import run_metadata
    timer = time.time()
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        if not direct:
            run_extract(processor, tree)
        else:
            tree.add("[green]✓[/green] Loaded pre-extracted text & tables from directory")
            
        run_metadata(processor, tree)
        run_summarise(processor, tree)
        processor.save_all()
        elapsed_time = time.time() - timer
        tree.add(f"Total time taken: [yellow]{elapsed_time:.2f}s[/yellow]")
        live.refresh()
        
    processor.cleanup()
