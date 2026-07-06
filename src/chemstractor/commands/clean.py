import sys
import os
import time
import glob
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.lib.cleaner import clean_csv
from chemstractor.AI import AI, pricing_matrix

def run_clean(processor: PDFProcessor, tree: Tree):
    """Executes the cleaning process on the processor and updates the rich Tree with status/pricing."""
    clean_node = tree.add(Spinner("dots", text="[bold cyan]Cleaning extracted tables...[/bold cyan]"))
    model = AI.get_instance().selected_model

    csv_dir = os.path.join(processor.tables_dir, "csv")
    if not os.path.exists(csv_dir):
        clean_node.label = "[yellow]⚠[/yellow] No extracted CSV tables found."
        return

    csv_files = sorted(glob.glob(os.path.join(csv_dir, "*.csv")))
    if not csv_files:
        clean_node.label = "[yellow]⚠[/yellow] No CSV tables to clean."
        return

    clean_dir = os.path.join(processor.output_dir, "clean")
    os.makedirs(clean_dir, exist_ok=True)

    timer = time.time()
    results = []

    for i, csv_path in enumerate(csv_files):
        table_name = os.path.basename(csv_path)
        clean_node.label = Spinner("dots", text=f"[bold cyan]Cleaning table {i + 1}/{len(csv_files)} ({table_name})...[/bold cyan]")

        output_path = os.path.join(clean_dir, table_name)
        
        # Execute the cleaning
        res = clean_csv(csv_path, output_path)
        results.append((table_name, res.success, res.error, res.usage_metadata))

    elapsed_time = time.time() - timer

    # Compute token counts/costs
    total_in = 0
    total_out = 0
    has_tokens = False
    for item in results:
        if len(item) == 4 and item[3]:
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

    clean_node.label = f"[green]✓[/green] Cleaned extracted tables using [magenta]{model}[/magenta] [dim](completed in {elapsed_time:.2f}s){tokens_title}[/dim]"

    for table_name, success, status, usage_metadata in results:
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
            clean_node.add(f"{table_name}: [bold green]Cleaned[/bold green]{tokens_str}")
        else:
            if "No diffusion coefficient column identified" in status:
                clean_node.add(f"{table_name}: [blue]Skipped (no diffusion column)[/blue]{tokens_str}")
            else:
                clean_node.add(f"{table_name}: [red]Failed: {status}[/red]")

def clean_command(
    process_output_dir: str
):
    console = Console(file=sys.__stdout__)
    
    # Initialize PDFProcessor using prepare_processor middleware
    from chemstractor.commands.utils import prepare_processor
    processor, output_dir = prepare_processor(
        pdf_path_or_dir=process_output_dir,
        output_dir=process_output_dir,
        direct=True,
        same_folder=True,
        suffix="cleaned"
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    tree.add("[green]✓[/green] Loaded pre-extracted text & tables from directory")
    
    timer = time.time()
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        run_clean(processor, tree)
        elapsed_time = time.time() - timer
        tree.add(f"Total time taken: [yellow]{elapsed_time:.2f}s[/yellow]")
        live.refresh()
        
    processor.cleanup()
