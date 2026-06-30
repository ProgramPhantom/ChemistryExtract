import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels

def extract_command(pdf_path: str, clean_dir: str, output_dir: str, logs_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
    console = Console(file=sys.__stdout__)
    base_name = os.path.basename(pdf_path)
    
    # Create directories if they do not exist
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
                
        live.refresh()
        
    processor.cleanup()
