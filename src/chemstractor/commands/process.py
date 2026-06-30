import os
import sys
import time
from rich.console import Console
from rich.tree import Tree
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels
from chemstractor.commands.extract import run_extract
from chemstractor.commands.categorise import run_categorise
from chemstractor.commands.summarise import run_summarise

def run_process_single(
    pdf_path: str,
    output_dir: str,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash",
    console: Console = None
) -> dict:
    """Runs extraction, categorisation, and summarisation on a single PDF."""
    if console is None:
        console = Console(file=sys.__stdout__)
        
    timer = time.time()
    
    # Initialize PDFProcessor
    processor = PDFProcessor(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=model
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        # 1. Extract
        run_extract(processor, tree)
        
        # 2. Categorise
        if categorise_tables:
            run_categorise(processor, tree)
            
        # 3. Summarise
        if summarise_tables:
            run_summarise(processor, tree)
            
        processor.save_all()
        live.refresh()
        
    elapsed_time = time.time() - timer
    num_tables = processor.num_tables
    processor.cleanup()
    
    return {
        "file": os.path.basename(pdf_path),
        "tables": num_tables,
        "time": elapsed_time
    }

def process_command(
    pdf_path: str,
    output_dir: str,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash"
):
    console = Console(file=sys.__stdout__)
    run_process_single(
        pdf_path=pdf_path,
        output_dir=output_dir,
        categorise_tables=categorise_tables,
        summarise_tables=summarise_tables,
        model=model,
        console=console
    )
