import os
import sys
from rich.console import Console
from rich.rule import Rule

from chemstractor.commands.interpret import interpret_command

def interpret_all_command(
    pdf_dir: str = None,
    output_parent_dir: str = None,
    direct: bool = False,
    flory: bool = True,
    mark_houwink: bool = False
):
    console = Console(file=sys.__stdout__)
    
    # Use the middleware helper to resolve directories and prepare extracts
    from chemstractor.commands.utils import prepare_batch_dirs
    pdf_dir, run_dir, items = prepare_batch_dirs(pdf_dir, output_parent_dir, direct=direct)
    
    console.print()
    label = "INTERPRETING PRE-EXTRACTED" if direct else "INTERPRETING ALL"
    console.print(Rule(title=f"[bold magenta]{label} {len(items)} ITEMS[/bold magenta]", style="magenta"))
    console.print()
    
    if direct:
        for dest_subdir_path in items:
            interpret_command(
                pdf_path=dest_subdir_path,
                output_dir=dest_subdir_path,
                direct=True,
                same_folder=True,
                flory=flory,
                mark_houwink=mark_houwink
            )
    else:
        for pdf_path in items:
            interpret_command(
                pdf_path=pdf_path,
                output_dir=run_dir,
                direct=False,
                flory=flory,
                mark_houwink=mark_houwink
            )
