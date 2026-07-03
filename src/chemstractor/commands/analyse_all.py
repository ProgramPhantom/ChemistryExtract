import os
import sys
import glob
import time
import shutil
from rich.console import Console
from rich.rule import Rule

from chemstractor.models import AllSupportedModels
from chemstractor.commands.process_all import setup_run_layout, print_summary_table
from chemstractor.commands.analyse import run_analyse_single

def analyse_all_command(
    input_parent_dir: str = None,
    output_parent_dir: str = None,
    categorise_tables: bool = True,
    summarise_tables: bool = True,
    model: AllSupportedModels = "gemini-2.5-flash"
):
    console = Console(file=sys.__stdout__)
    
    # Resolve input_parent_dir: by default, the most recent folder in tests/runs
    runs_parent = "./tests/runs"
    if not os.path.exists(runs_parent):
        runs_parent = "tests/runs"
        
    if input_parent_dir is None:
        if os.path.exists(runs_parent):
            subdirs = [
                d for d in os.listdir(runs_parent)
                if os.path.isdir(os.path.join(runs_parent, d))
            ]
            if subdirs:
                subdirs.sort()
                input_parent_dir = os.path.join(runs_parent, subdirs[-1])
            else:
                console.print("[bold red]Error: No run folders found in tests/runs/ to use as input.[/bold red]")
                sys.exit(1)
        else:
            console.print("[bold red]Error: tests/runs/ directory does not exist and no input path was provided.[/bold red]")
            sys.exit(1)
            
    if output_parent_dir is None:
        output_parent_dir = runs_parent
        
    if not os.path.exists(input_parent_dir) or not os.path.isdir(input_parent_dir):
        console.print(f"[bold red]Error: Input directory '{input_parent_dir}' does not exist or is not a directory.[/bold red]")
        sys.exit(1)
        
    # Scan for folders that contain an "extract" folder with extracted data
    subdirs = []
    for name in os.listdir(input_parent_dir):
        path = os.path.join(input_parent_dir, name)
        if os.path.isdir(path):
            extract_path = os.path.join(path, "extract")
            if os.path.isdir(extract_path) and os.path.isfile(os.path.join(extract_path, "output.md")):
                subdirs.append(path)
                
    if not subdirs:
        console.print(f"[bold red]Error: No folders containing pre-extracted data (an 'extract' subfolder with output.md) were found in '{input_parent_dir}'.[/bold red]")
        sys.exit(1)
        
    console.print()
    console.print(Rule(title=f"[bold magenta]ANALYSING {len(subdirs)} FOLDERS[/bold magenta]", style="magenta"))
    console.print()
    
    # 1. Setup timestamped run directory
    run_dir = setup_run_layout(output_parent_dir)
    
    summary_data = []
    
    for src_subdir_path in subdirs:
        base_name = os.path.basename(src_subdir_path)
        dest_subdir_path = os.path.join(run_dir, base_name)
        
        # Copy extract folder as-is
        src_extract = os.path.join(src_subdir_path, "extract")
        dest_extract = os.path.join(dest_subdir_path, "extract")
        os.makedirs(dest_subdir_path, exist_ok=True)
        shutil.copytree(src_extract, dest_extract)
        
        res = run_analyse_single(
            output_dir=dest_subdir_path,
            categorise_tables=categorise_tables,
            summarise_tables=summarise_tables,
            model=model,
            console=console
        )
        summary_data.append(res)
        
    # Print the final summary table
    print_summary_table(console, summary_data)
