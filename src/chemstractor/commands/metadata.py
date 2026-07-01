import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels, pricing_matrix
from chemstractor.commands.extract import run_extract


def run_metadata(processor: PDFProcessor, tree: Tree):
    """Executes the metadata extraction process on the processor and updates the rich Tree with status/pricing."""
    meta_node = tree.add(Spinner("dots", text="[bold cyan]Extracting paper-level metadata...[/bold cyan]"))
    model = processor.model

    for event in processor.extract_metadata():
        if event["status"] == "working":
            meta_node.label = Spinner("dots", text=f"[bold cyan]{event['message']}[/bold cyan]")
            
        elif event["status"] == "complete":
            elapsed_time = event["elapsed_time"]
            success = event["success"]
            error = event["error"]
            usage_metadata = event["usage_metadata"]
            
            tokens_title = ""
            if success and usage_metadata:
                cost_str = ""
                in_t = usage_metadata.get("prompt_token_count", 0)
                out_t = usage_metadata.get("candidates_token_count", 0)
                if model in pricing_matrix:
                    pricing = pricing_matrix[model]
                    cost = (in_t * pricing["input_per_m"] + out_t * pricing["output_per_m"]) / 1_000_000
                    cost_str = f"; Cost: ${cost:.6f}"
                tokens_title = f" (tokens: {in_t} in, {out_t} out{cost_str})"
                
            if success:
                meta_node.label = f"[green]✓[/green] Extracted paper-level metadata using [magenta]{model}[/magenta] [dim](completed in {elapsed_time:.2f}s){tokens_title}[/dim]"
                if processor.metadata_res and processor.metadata_res.data:
                    data = processor.metadata_res.data
                    meta_node.add(f"Title: {data.title}")
                    meta_node.add(f"Authors: {', '.join(data.authors)}")
                    meta_node.add(f"DOI: {data.doi}")
            else:
                meta_node.label = f"[red]✗[/red] Failed to extract paper-level metadata: [red]{error}[/red]"


def metadata_command(pdf_path: str, output_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
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
        run_metadata(processor, tree)
        processor.save_all()
        live.refresh()
        
    processor.cleanup()
