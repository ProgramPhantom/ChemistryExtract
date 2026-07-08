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

def run_categorise(processor: PDFProcessor, tree: Tree):
    """Executes the categorisation process on the processor and updates the rich Tree with status/pricing."""
    cat_node = tree.add(Spinner("dots", text="[bold cyan]Categorising extracted tables...[/bold cyan]"))
    model = AI.get_instance().selected_model
    for event in processor.categorise():
        if event["status"] == "working" or event["status"] == "table_start":
            cat_node.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
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
                for idx, item in enumerate(cat_results):
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
                        if status == "Not flagged":
                            reasons = []
                            cat_data = processor.cat_data_list[idx] if idx < len(processor.cat_data_list) else None
                            if cat_data:
                                if not cat_data.get("contains_scientific_data", False):
                                    reasons.append("no experimental data")
                                if not cat_data.get("contains_polymer_diffusion_coeff", False):
                                    reasons.append("no polymers")
                            reasons_str = f" ({', '.join(reasons)})" if reasons else ""
                            status_styled = f"[blue]{status}{reasons_str}[/blue]"
                        elif status == "unsure":
                            status_styled = f"[yellow]{status}[/yellow]"
                        elif any(x in status for x in ["raw", "coeff", "mark_houwink", "flory"]):
                            status_styled = f"[bold green]{status}[/bold green]"
                        else:
                            status_styled = f"[blue]{status}[/blue]"
                        cat_node.add(f"{table_name}: {status_styled}{tokens_str}")
                    else:
                        cat_node.add(f"{table_name}: [red]{status}[/red]")

def categorise_command(
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
        suffix="categorised"
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    timer = time.time()
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        if not direct:
            run_extract(processor, tree)
        else:
            tree.add("[green]✓[/green] Loaded pre-extracted text & tables from directory")
            
        run_categorise(processor, tree)
        processor.save_all()
        elapsed_time = time.time() - timer
        tree.add(f"Total time taken: [yellow]{elapsed_time:.2f}s[/yellow]")
        live.refresh()
        
    processor.cleanup()
