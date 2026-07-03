import os
import sys
import time
from rich.console import Console
from rich.tree import Tree
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels
from chemstractor.commands.categorise import run_categorise
from chemstractor.commands.summarise import run_summarise
from chemstractor.commands.metadata import run_metadata

def run_analyse_single(
    output_dir: str,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash",
    console: Console = None
) -> dict:
    """Runs metadata extraction, table categorisation, and summarisation using pre-extracted data."""
    if console is None:
        console = Console(file=sys.__stdout__)
        
    timer = time.time()
    
    # Initialize PDFProcessor
    processor = PDFProcessor(model=model)
    # Load configuration from output directory paths
    processor.load_output(output_dir)
    
    tree = Tree(f"[bold cyan]📄 {processor.base_name}[/bold cyan]")
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        # 1. Metadata
        run_metadata(processor, tree)
        
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
        "file": os.path.basename(output_dir),
        "tables": num_tables,
        "time": elapsed_time
    }

def analyse_command(
    process_output_dir: str,
    same_folder: bool,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash"
):
    import shutil
    console = Console(file=sys.__stdout__)
    
    # Check that it contains an "extract" subfolder containing the extracted data
    extract_dir = os.path.join(process_output_dir, "extract")
    if not os.path.isdir(extract_dir) or not os.path.isfile(os.path.join(extract_dir, "output.md")):
        console.print(f"[bold red]Error: The input folder '{process_output_dir}' must contain an 'extract' subfolder with extracted data (e.g. output.md).[/bold red]")
        sys.exit(1)

    if same_folder:
        output_dir = process_output_dir
    else:
        # Create a new pdf output folder next to the input folder
        input_abs = os.path.abspath(os.path.normpath(process_output_dir))
        parent_dir = os.path.dirname(input_abs)
        base_name = os.path.basename(input_abs)
        
        # New folder next to the input folder
        new_dir = os.path.join(parent_dir, f"{base_name}_analysed")
        
        # Copy the extract from the input folder to the new output folder as it is
        console.print(f"Creating new output folder and copying extract to: [yellow]{new_dir}[/yellow]")
        new_extract_dir = os.path.join(new_dir, "extract")
        os.makedirs(new_dir, exist_ok=True)
        if os.path.exists(new_extract_dir):
            shutil.rmtree(new_extract_dir)
        shutil.copytree(extract_dir, new_extract_dir)
        output_dir = new_dir

    run_analyse_single(
        output_dir=output_dir,
        categorise_tables=categorise_tables,
        summarise_tables=summarise_tables,
        model=model,
        console=console
    )
