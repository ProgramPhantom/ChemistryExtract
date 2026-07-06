import os
import sys
from rich.console import Console
from rich.rule import Rule

from chemstractor.commands.clean import clean_command

def clean_all_command(outputs_dir: str = None):
    console = Console(file=sys.__stdout__)
    
    runs_parent = "./tests/runs"
    if not os.path.exists(runs_parent):
        runs_parent = "tests/runs"
        
    if outputs_dir is None:
        if os.path.exists(runs_parent):
            subdirs = [
                d for d in os.listdir(runs_parent)
                if os.path.isdir(os.path.join(runs_parent, d))
            ]
            if subdirs:
                subdirs.sort()
                outputs_dir = os.path.join(runs_parent, subdirs[-1])
            else:
                console.print("[bold red]Error: No run folders found in tests/runs/ to clean.[/bold red]")
                return
        else:
            console.print("[bold red]Error: tests/runs/ directory does not exist and no outputs path was provided.[/bold red]")
            return

    if not os.path.exists(outputs_dir):
        console.print(f"[bold red]Error: Outputs directory '{outputs_dir}' does not exist.[/bold red]")
        return

    # Grab all subdirectories in outputs_dir
    subfolders = [
        os.path.join(outputs_dir, d) for d in os.listdir(outputs_dir)
        if os.path.isdir(os.path.join(outputs_dir, d))
    ]
    
    # Filter only those that have extract directory or tables
    valid_subfolders = []
    for sf in subfolders:
        extract_dir = os.path.join(sf, "extract")
        if os.path.isdir(extract_dir):
            valid_subfolders.append(sf)

    if not valid_subfolders:
        console.print("[bold red]Error: No subfolders containing pre-extracted data found to clean.[/bold red]")
        return

    console.print(Rule(title=f"[bold magenta]CLEANING ALL OUTPUTS ({len(valid_subfolders)} ITEMS)[/bold magenta]", style="magenta"))
    console.print(f"Outputs path: [cyan]{outputs_dir}[/cyan]")
    console.print()

    for sf in sorted(valid_subfolders):
        clean_command(sf)
