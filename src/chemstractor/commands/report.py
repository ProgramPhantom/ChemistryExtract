import os
import sys
from rich.console import Console
from chemstractor.lib.processor import PDFProcessor

def report_command(process_output_dir: str, output: str = None) -> None:
    """Reads a process output folder, gathers all data, and generates an Excel report."""
    console = Console(file=sys.__stdout__)
    
    if not os.path.exists(process_output_dir):
        console.print(f"[bold red]Error: Process output directory '{process_output_dir}' does not exist.[/bold red]")
        return
        
    if not os.path.isdir(process_output_dir):
        console.print(f"[bold red]Error: '{process_output_dir}' is not a directory.[/bold red]")
        return

    try:
        processor = PDFProcessor()
        processor.load_output(process_output_dir)
        
        if processor.num_tables == 0:
            console.print(f"[bold red]Error: No table data found in '{process_output_dir}'.[/bold red]")
            return
            
        # Resolve destination path
        if output is None:
            output_filename = f"{processor.base_no_ext}_summary.xlsx"
            dest_path = os.path.join(processor.output_dir, output_filename)
        else:
            if os.path.isdir(output):
                output_filename = f"{processor.base_no_ext}_summary.xlsx"
                dest_path = os.path.join(output, output_filename)
            else:
                # Ensure the directory of output exists
                dest_dir = os.path.dirname(output)
                if dest_dir and not os.path.exists(dest_dir):
                    os.makedirs(dest_dir, exist_ok=True)
                dest_path = output
                
        # Generate the report
        processor.create_excel(dest_path=dest_path)
        console.print(f"[bold green]✓[/bold green] Excel report successfully created at: [cyan]{dest_path}[/cyan]")
    except Exception as e:
        console.print(f"[bold red]Error: Failed to create Excel report: {e}[/bold red]")
        return


