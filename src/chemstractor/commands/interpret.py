import sys
import os
import time
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.AI import AI, pricing_matrix

def run_interpret(processor: PDFProcessor, tree: Tree):
    """Executes the interpretation process on the processor and updates the rich Tree with status/pricing/calculator calls."""
    interpret_node = tree.add(Spinner("dots", text="[bold cyan]Interpreting coeff tables...[/bold cyan]"))
    model = AI.get_instance().selected_model
    
    # Check if there are any tables loaded
    if processor.num_tables == 0:
        interpret_node.label = "[yellow]⚠[/yellow] No extracted tables found to interpret."
        return

    # Check if we have categorisation data loaded and if any are coeff
    has_coeff = False
    for i in range(processor.num_tables):
        cat_data = processor.cat_data_list[i] if i < len(processor.cat_data_list) else None
        if cat_data and cat_data.get("contains_diffusion_coeff") == "coeff":
            has_coeff = True
            break
            
    if not has_coeff:
        interpret_node.label = "[yellow]⚠[/yellow] No tables categorized as [bold green]coeff[/bold green] found. Skipping interpretation."
        return

    for event in processor.interpret():
        if event["status"] == "working" or event["status"] == "table_start":
            interpret_node.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
        elif event["status"] == "complete":
            elapsed_time = event["elapsed_time"]
            interpret_results = event["results"]
            
            # Compute token counts/costs
            total_in = 0
            total_out = 0
            has_tokens = False
            for item in interpret_results:
                if len(item) >= 4 and item[3]:
                    total_in += item[3].get("prompt_token_count", 0) or 0
                    total_out += item[3].get("candidates_token_count", 0) or 0
                    has_tokens = True
                    
            tokens_title = ""
            if has_tokens:
                cost_str = ""
                if model in pricing_matrix:
                    pricing = pricing_matrix[model]
                    cost = (total_in * pricing["input_per_m"] + total_out * pricing["output_per_m"]) / 1_000_000
                    cost_str = f"; Cost: ${cost:.6f}"
                tokens_title = f" (Total tokens: {total_in} in, {total_out} out{cost_str})"
                
            interpret_node.label = f"[green]✓[/green] Interpreted coeff tables using [magenta]{model}[/magenta] [dim](completed in {elapsed_time:.2f}s){tokens_title}[/dim]"
            
            for item in interpret_results:
                table_name = item[0]
                success = item[1]
                status = item[2]
                usage_metadata = item[3]
                calc_calls = item[4] if len(item) >= 5 else []
                
                tokens_str = ""
                if usage_metadata:
                    in_t = usage_metadata.get("prompt_token_count", 0) or 0
                    out_t = usage_metadata.get("candidates_token_count", 0) or 0
                    cost_item_str = ""
                    if model in pricing_matrix:
                        pricing = pricing_matrix[model]
                        cost_item = (in_t * pricing["input_per_m"] + out_t * pricing["output_per_m"]) / 1_000_000
                        cost_item_str = f"; Cost: ${cost_item:.6f}"
                    tokens_str = f" [dim](tokens: {in_t} in, {out_t} out{cost_item_str})[/dim]"
                    
                if success:
                    if status == "Skipped (not coeff)":
                        interpret_node.add(f"{table_name}: [blue]{status}[/blue]")
                    else:
                        table_node = interpret_node.add(f"{table_name}: [bold green]Interpreted[/bold green]{tokens_str}")
                        if calc_calls:
                            for cc in calc_calls:
                                table_node.add(f"[yellow]Calculator Call:[/yellow] [cyan]{cc['expression']}[/cyan] -> [green]{cc['result']}[/green]")
                else:
                    table_node = interpret_node.add(f"{table_name}: [red]{status}[/red]")
                    if calc_calls:
                        for cc in calc_calls:
                            table_node.add(f"[yellow]Calculator Call:[/yellow] [cyan]{cc['expression']}[/cyan] -> [green]{cc['result']}[/green]")


def interpret_command(
    pdf_path: str,
    output_dir: str,
    direct: bool = False,
    same_folder: bool = True
):
    console = Console(file=sys.__stdout__)
    
    from chemstractor.commands.utils import prepare_processor
    processor, output_dir = prepare_processor(
        pdf_path_or_dir=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder,
        suffix="interpreted"
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    if direct:
        tree.add("[green]✓[/green] Loaded pre-extracted text & tables from directory")
    else:
        from chemstractor.commands.extract import run_extract
        from chemstractor.commands.categorise import run_categorise
        from chemstractor.commands.metadata import run_metadata
        
        timer = time.time()
        with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
            run_extract(processor, tree)
            run_categorise(processor, tree)
            run_metadata(processor, tree)
            live.refresh()
            
    timer = time.time()
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        run_interpret(processor, tree)
        processor.save_all()
        elapsed_time = time.time() - timer
        tree.add(f"Total time taken for interpretation: [yellow]{elapsed_time:.2f}s[/yellow]")
        live.refresh()
        
    processor.cleanup()
