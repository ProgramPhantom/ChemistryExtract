import os
import sys
import glob
import json
from rich.console import Console
from rich.rule import Rule
from rich.tree import Tree

def validate_extract(output_subfolder: str, validation_subfolder: str, parent: Tree):
    """Placeholder function for validating extraction process."""
    node = parent.add("[bold blue]Checking extraction (not implemented)...[/bold blue]")
    node.add("[dim]Extraction validation logic will go here.[/dim]")

def validate_categorise(output_subfolder: str, validation_subfolder: str, parent: Tree):
    """Compares categorisation JSON outputs against validation data."""
    node = parent.add("[bold blue]Checking categorisation...[/bold blue]")
    
    out_cat_dir = os.path.join(output_subfolder, "categorisation")
    val_cat_dir = os.path.join(validation_subfolder, "categorisation")
    
    if not os.path.exists(out_cat_dir):
        node.add("[red]✗[/red] Output categorisation folder does not exist.")
        return
        
    if not os.path.exists(val_cat_dir):
        node.add("[red]✗[/red] Validation categorisation folder does not exist.")
        return
        
    val_files = glob.glob(os.path.join(val_cat_dir, "*.json"))
    out_files = glob.glob(os.path.join(out_cat_dir, "*.json"))
    
    if not val_files:
        node.add("[yellow]⚠[/yellow] No JSON files found in validation categorisation folder.")
        return
        
    val_basenames = {os.path.basename(f) for f in val_files}
    out_basenames = {os.path.basename(f) for f in out_files}
    
    all_tables = sorted(list(val_basenames.union(out_basenames)))
    
    for table_file in all_tables:
        table_node = node.add(f"[bold]Table: {table_file}[/bold]")
        
        val_path = os.path.join(val_cat_dir, table_file)
        out_path = os.path.join(out_cat_dir, table_file)
        
        if not os.path.exists(val_path):
            table_node.add("[yellow]✗[/yellow] Table is only present in run output (missing from validation data).")
            continue
            
        if not os.path.exists(out_path):
            table_node.add("[red]✗[/red] Table is missing from run output.")
            continue
            
        # Compare key-value pairs
        try:
            with open(val_path, 'r', encoding='utf-8') as f:
                val_data = json.load(f)
        except Exception as e:
            table_node.add(f"[red]✗[/red] Error reading validation file: {e}")
            continue
            
        try:
            with open(out_path, 'r', encoding='utf-8') as f:
                out_data = json.load(f)
        except Exception as e:
            table_node.add(f"[red]✗[/red] Error reading output file: {e}")
            continue
            
        all_keys = set(val_data.keys()).union(set(out_data.keys()))
        
        matches = []
        mismatches = []
        only_val = []
        only_out = []
        
        for key in sorted(all_keys):
            if key in val_data and key in out_data:
                if val_data[key] == out_data[key]:
                    matches.append((key, val_data[key]))
                else:
                    mismatches.append((key, val_data[key], out_data[key]))
            elif key in val_data:
                only_val.append((key, val_data[key]))
            else:
                only_out.append((key, out_data[key]))
                
        total_keys = len(all_keys)
        match_count = len(matches)
        match_pct = (match_count / total_keys * 100) if total_keys > 0 else 0.0
        
        table_node.add(f"Match Percentage: [bold]{match_pct:.1f}%[/bold] ({match_count}/{total_keys} fields)")
        
        if matches:
            matches_node = table_node.add("[green]Matching fields:[/green]")
            for k, val in matches:
                matches_node.add(f"✓ {k}: {val}")
        if mismatches:
            mismatches_node = table_node.add("[red]Mismatches:[/red]")
            for k, expected, got in mismatches:
                mismatches_node.add(f"✗ {k}: Expected {expected}, got {got}")
        if only_val:
            only_val_node = table_node.add("[yellow]Only in validation data:[/yellow]")
            for k, val in only_val:
                only_val_node.add(f"? {k}: {val}")
        if only_out:
            only_out_node = table_node.add("[yellow]Only in output data:[/yellow]")
            for k, val in only_out:
                only_out_node.add(f"? {k}: {val}")

def validate_summarise(output_subfolder: str, validation_subfolder: str, parent: Tree):
    """Placeholder function for validating summarisation process."""
    node = parent.add("[bold blue]Checking summarisation (not implemented)...[/bold blue]")
    node.add("[dim]Summarisation validation logic will go here.[/dim]")

def run_validate(output_dir: str, validation_dir: str, subfolders: list[str], console: Console):
    """Coordinates the validation processes across all matching subfolders."""
    for sub in subfolders:
        out_sub_path = os.path.join(output_dir, sub)
        val_sub_path = os.path.join(validation_dir, sub)
        run_validate_single(out_sub_path, val_sub_path, sub, console)

def run_validate_single(output_subfolder: str, validation_subfolder: str, name: str, console: Console):
    """Validates a single PDF run folder against its correct validation data using a Tree."""
    tree = Tree(f"[bold green]Validating {name}[/bold green]")
    
    # 1. Validate extract
    validate_extract(output_subfolder, validation_subfolder, tree)
    
    # 2. Validate categorise
    validate_categorise(output_subfolder, validation_subfolder, tree)
    
    # 3. Validate summarise
    validate_summarise(output_subfolder, validation_subfolder, tree)
    
    console.print(tree)
    console.print()

def validate_command(output_dir: str, validation_dir: str):
    """
    Validates extracted PDF outputs against correct validation data.
    Supports both parent directories containing multiple runs, and leaf run directories.
    """
    console = Console(file=sys.__stdout__)
    console.print(Rule(title="[bold yellow]VALIDATING OUTPUTS[/bold yellow]", style="yellow"))
    console.print(f"Output directory: [cyan]{output_dir}[/cyan]")
    console.print(f"Validation directory: [cyan]{validation_dir}[/cyan]")
    console.print()
    
    if not os.path.exists(output_dir):
        console.print(f"[bold red]Error: Output directory '{output_dir}' does not exist.[/bold red]")
        return
        
    if not os.path.exists(validation_dir):
        console.print(f"[bold red]Error: Validation directory '{validation_dir}' does not exist.[/bold red]")
        return

    # Determine if they are leaf run directories directly
    out_is_leaf = os.path.exists(os.path.join(output_dir, "categorisation")) or os.path.exists(os.path.join(output_dir, "extract"))
    val_is_leaf = os.path.exists(os.path.join(validation_dir, "categorisation")) or os.path.exists(os.path.join(validation_dir, "extract"))
    
    if out_is_leaf and val_is_leaf:
        # Validate directly as a single run folder
        run_validate_single(output_dir, validation_dir, os.path.basename(output_dir), console)
    elif out_is_leaf or val_is_leaf:
        console.print("[bold red]Error: Mismatched directory levels. One directory seems to be a run folder, while the other is a parent folder.[/bold red]")
        return
    else:
        # Scan for matching subfolders
        out_subfolders = {d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))}
        val_subfolders = {d for d in os.listdir(validation_dir) if os.path.isdir(os.path.join(validation_dir, d))}
        
        common = sorted(list(out_subfolders.intersection(val_subfolders)))
        only_out = sorted(list(out_subfolders - val_subfolders))
        only_val = sorted(list(val_subfolders - out_subfolders))
        
        if only_out:
            console.print(f"[yellow]Note: The following folders are only in output directory and won't be validated: {', '.join(only_out)}[/yellow]")
        if only_val:
            console.print(f"[yellow]Note: The following folders are only in validation directory and won't be validated: {', '.join(only_val)}[/yellow]")
            
        if not common:
            console.print("[bold red]Error: No matching subfolders found to validate.[/bold red]")
            return
            
        run_validate(output_dir, validation_dir, common, console)
