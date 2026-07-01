import os
import sys
import json
import csv
from rich.console import Console
from chemstractor.lib.report import create_excel

def report_command(process_output_dir: str, output: str = None) -> None:
    """Reads a process output folder, gathers all data, and generates an Excel report."""
    console = Console(file=sys.__stdout__)
    
    if not os.path.exists(process_output_dir):
        console.print(f"[bold red]Error: Process output directory '{process_output_dir}' does not exist.[/bold red]")
        sys.exit(1)
        
    if not os.path.isdir(process_output_dir):
        console.print(f"[bold red]Error: '{process_output_dir}' is not a directory.[/bold red]")
        sys.exit(1)

    base_no_ext = os.path.basename(os.path.normpath(process_output_dir))
    
    # 1. Gather Metadata
    summary_json_path = os.path.join(process_output_dir, "summary", "summary.json")
    metadata = {}
    if os.path.exists(summary_json_path):
        try:
            with open(summary_json_path, 'r', encoding='utf-8') as mf:
                metadata = json.load(mf)
        except Exception as e:
            console.print(f"[yellow]Warning: Error loading metadata JSON {summary_json_path}: {e}[/yellow]")
            
    # 2. Scan and Gather Tables
    csv_dir = os.path.join(process_output_dir, "extract", "tables", "csv")
    num_tables = 0
    if os.path.exists(csv_dir):
        while os.path.exists(os.path.join(csv_dir, f"table{num_tables + 1}.csv")):
            num_tables += 1
            
    if num_tables == 0:
        console.print(f"[bold red]Error: No table data found in '{process_output_dir}' (checked '{csv_dir}').[/bold red]")
        sys.exit(1)
        
    tables_data = []
    for i in range(num_tables):
        table_json_path = os.path.join(process_output_dir, "summary", "tables", f"table{i + 1}.json")
        csv_path = os.path.join(csv_dir, f"table{i + 1}.csv")
        cat_path = os.path.join(process_output_dir, "categorisation", f"table{i + 1}.json")
        
        table_data = {}
        if os.path.exists(table_json_path):
            try:
                with open(table_json_path, 'r', encoding='utf-8') as jf:
                    table_data = json.load(jf)
            except Exception as e:
                console.print(f"[yellow]Warning: Error loading table JSON {table_json_path}: {e}[/yellow]")
                
        cat_data = {}
        if os.path.exists(cat_path):
            try:
                with open(cat_path, 'r', encoding='utf-8') as cf:
                    cat_data = json.load(cf)
            except Exception as e:
                console.print(f"[yellow]Warning: Error loading categorisation JSON {cat_path}: {e}[/yellow]")
                
        csv_rows = None
        csv_error = None
        if os.path.exists(csv_path):
            try:
                with open(csv_path, 'r', encoding='utf-8', newline='') as cf:
                    reader = csv.reader(cf)
                    csv_rows = list(reader)
            except Exception as e:
                csv_error = str(e)
                console.print(f"[yellow]Warning: Error parsing CSV {csv_path}: {e}[/yellow]")
                
        tables_data.append({
            "table_data": table_data,
            "cat_data": cat_data,
            "csv_rows": csv_rows,
            "csv_error": csv_error
        })
        
    # 3. Resolve destination path
    if output is None:
        output_filename = f"{base_no_ext}_summary.xlsx"
        dest_path = os.path.join(process_output_dir, output_filename)
    else:
        if os.path.isdir(output):
            output_filename = f"{base_no_ext}_summary.xlsx"
            dest_path = os.path.join(output, output_filename)
        else:
            # Ensure the directory of output exists
            dest_dir = os.path.dirname(output)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir, exist_ok=True)
            dest_path = output
            
    # 4. Generate the report
    try:
        create_excel(
            dest_path=dest_path,
            base_no_ext=base_no_ext,
            metadata=metadata,
            tables_data=tables_data
        )
        console.print(f"[bold green]✓[/bold green] Excel report successfully created at: [cyan]{dest_path}[/cyan]")
    except Exception as e:
        console.print(f"[bold red]Error: Failed to create Excel report: {e}[/bold red]")
        sys.exit(1)
