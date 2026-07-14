import os
import sys
import time
from rich.console import Console
from rich.tree import Tree
from rich.live import Live

from chemstractor.commands.extract import run_extract
from chemstractor.commands.categorise import run_categorise
from chemstractor.commands.summarise import run_summarise
from chemstractor.commands.metadata import run_metadata

def run_process_single(
    pdf_path: str,
    output_dir: str,
    console: Console = None,
    direct: bool = False,
    same_folder: bool = True,
    interpret: bool = False,
    report: bool = False
) -> dict:
    """Runs extraction, categorisation, and summarisation on a single PDF."""
    if console is None:
        console = Console(file=sys.__stdout__)
        
    timer = time.time()
    
    # Initialize PDFProcessor using prepare_processor middleware
    from chemstractor.commands.utils import prepare_processor
    processor, output_dir = prepare_processor(
        pdf_path_or_dir=pdf_path,
        output_dir=output_dir,
        direct=direct,
        same_folder=same_folder,
        suffix="processed"
    )
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        # 1. Extract
        if not direct:
            run_extract(processor, tree)
        else:
            tree.add("[green]✓[/green] Loaded pre-extracted text & tables from directory")
        
        # 2. Categorise
        run_categorise(processor, tree)
            
        # 3. Metadata
        run_metadata(processor, tree)
            
        # 4. Summarise
        run_summarise(processor, tree)
            
        # 5. Interpret (if flag is present)
        if interpret:
            from chemstractor.commands.interpret import run_interpret
            run_interpret(processor, tree)
            
        processor.save_all()
        elapsed_time = time.time() - timer
        tree.add(f"Total time taken: [yellow]{elapsed_time:.2f}s[/yellow]")
        live.refresh()
        
    num_tables = processor.num_tables
    processor.cleanup()
    
    if report:
        from chemstractor.commands.report import report_command
        report_command(process_output_dir=processor.output_dir)
    
    return {
        "file": os.path.basename(pdf_path) if not direct else os.path.basename(output_dir),
        "tables": num_tables,
        "time": elapsed_time
    }

def process_command(
    pdf_path: str,
    output_dir: str,
    direct: bool = False,
    same_folder: bool = True,
    interpret: bool = False,
    report: bool = False
):
    console = Console(file=sys.__stdout__)
    run_process_single(
        pdf_path=pdf_path,
        output_dir=output_dir,
        console=console,
        direct=direct,
        same_folder=same_folder,
        interpret=interpret,
        report=report
    )
