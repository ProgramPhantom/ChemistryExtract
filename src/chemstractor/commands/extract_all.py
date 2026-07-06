import os
import sys
from rich.console import Console
from rich.rule import Rule

from chemstractor.commands.extract import extract_command
from chemstractor.commands.utils import prepare_batch_dirs

def extract_all_command(
    pdf_dir: str,
    output_parent_dir: str
):
    console = Console(file=sys.__stdout__)
    
    # Use the middleware helper to resolve directories
    pdf_dir, run_dir, pdf_files = prepare_batch_dirs(pdf_dir, output_parent_dir, direct=False)
    
    console.print()
    console.print(Rule(title=f"[bold magenta]EXTRACTING FROM {len(pdf_files)} ITEMS[/bold magenta]", style="magenta"))
    console.print()
    
    for pdf_path in pdf_files:
        extract_command(
            pdf_path=pdf_path,
            output_dir=run_dir
        )
