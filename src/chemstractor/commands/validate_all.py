import os
import sys
from rich.console import Console
from rich.rule import Rule
from chemstractor.commands.validate import run_validate

def validate_command(outputs_dir: str, validation_dir: str):
    """Validate all output folders in the given path against validation data."""
    console = Console(file=sys.__stdout__)
    
    if not os.path.exists(outputs_dir):
        console.print(f"[bold red]Error: Outputs directory '{outputs_dir}' does not exist.[/bold red]")
        return
        
    if not os.path.exists(validation_dir):
        console.print(f"[bold red]Error: Validation directory '{validation_dir}' does not exist.[/bold red]")
        return

    console.print(Rule(title="[bold yellow]VALIDATING ALL OUTPUTS[/bold yellow]", style="yellow"))
    console.print(f"Outputs path: [cyan]{outputs_dir}[/cyan]")
    console.print(f"Validation path: [cyan]{validation_dir}[/cyan]")
    console.print()
    
    # Grab all subdirectories in outputs_dir
    out_subfolders = {d for d in os.listdir(outputs_dir) if os.path.isdir(os.path.join(outputs_dir, d))}
    val_subfolders = {d for d in os.listdir(validation_dir) if os.path.isdir(os.path.join(validation_dir, d))}
    
    common = sorted(list(out_subfolders.intersection(val_subfolders)))
    only_out = sorted(list(out_subfolders - val_subfolders))
    
    if only_out:
        console.print(f"[yellow]Note: The following folders are only in outputs directory and won't be validated: {', '.join(only_out)}[/yellow]")
        console.print()
        
    if not common:
        console.print("[bold red]Error: No matching subfolders found to validate.[/bold red]")
        return
        
    run_validate(outputs_dir, validation_dir, common, console)
