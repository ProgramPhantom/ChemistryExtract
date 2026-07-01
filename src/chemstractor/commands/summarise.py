import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels, pricing_matrix
from chemstractor.commands.extract import run_extract

def run_summarise(processor: PDFProcessor, tree: Tree):
    """Executes the summarisation process on the processor and updates the rich Tree with status/pricing."""

    sum_node = tree.add(Spinner("dots", text="[bold cyan]Summarising experimental conditions...[/bold cyan]"))
    model = processor.model

    for event in processor.summarise():

        if event["status"] == "working" or event["status"] == "table_start":
            sum_node.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
            
        elif event["status"] == "complete":
            elapsed_time = event["elapsed_time"]
            sum_results = event["results"]
            metadata_res = processor.metadata_res
            
            # Compute token counts/costs
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

def summarise_command(pdf_path: str, output_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
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
        run_summarise(processor, tree)
        processor.save_all()
        live.refresh()
        
    processor.cleanup()
