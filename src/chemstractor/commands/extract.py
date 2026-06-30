import sys
import os
from rich.console import Console
from rich.tree import Tree
from rich.spinner import Spinner
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.models import AllSupportedModels

def get_hardware_acceleration_backends() -> list[str]:
    """Detects available hardware acceleration backends (CUDA, MPS, DirectML)."""
    backends = []
    try:
        import torch
        if torch.cuda.is_available():
            backends.append(f"CUDA ({torch.cuda.get_device_name(0)})")
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            backends.append("Apple MPS")
    except ImportError:
        pass

    try:
        import onnxruntime as ort
        if "DmlExecutionProvider" in ort.get_available_providers():
            backends.append("DirectML (AMD/Intel GPU)")
    except ImportError:
        pass

    return backends


def run_extract(processor: PDFProcessor, tree: Tree):
    """Executes the extraction process on the processor and updates the rich Tree with status/logs."""
    ext_node = tree.add(Spinner("dots", text="[bold cyan]Extracting text & tables...[/bold cyan]"))
    
    # Check and display GPU acceleration status
    gpu_backends = get_hardware_acceleration_backends()
    if gpu_backends:
        gpu_str = ", ".join(gpu_backends)
        ext_node.add(f"Hardware Acceleration: [green]GPU Active ({gpu_str})[/green]")
    else:
        ext_node.add("Hardware Acceleration: [yellow]CPU[/yellow]")

    for event in processor.extract():
        if event["status"] == "complete":
            elapsed_time = event["elapsed_time"]
            num_tables = event["num_tables"]
            
            ext_node.label = f"[green]✓[/green] Extracted text & tables [dim](completed in {elapsed_time:.2f}s)[/dim]"
            ext_node.add("Extracted text & tables in-memory")
            ext_node.add(f"Saved cleaned PDF to [yellow]{os.path.relpath(processor.clean_path)}[/yellow]")
            ext_node.add(f"Saved parsed markdown to [yellow]{os.path.relpath(processor.parsed_md_path)}[/yellow]")
            ext_node.add(f"Saved {num_tables} tables (txt & csv) to [yellow]{os.path.relpath(processor.tables_dir)}[/yellow]")
            ext_node.add(f"Saved execution logs to [yellow]{os.path.relpath(processor.log_file_path)}[/yellow]")

def extract_command(pdf_path: str, output_dir: str, model: AllSupportedModels = "gemini-2.5-flash"):
    console = Console(file=sys.__stdout__)
    base_name = os.path.basename(pdf_path)
    
    tree = Tree(f"[bold cyan]📄 {base_name}[/bold cyan]")
    
    processor = PDFProcessor(
        pdf_path=pdf_path,
        output_dir=output_dir,
        model=model
    )
    
    with Live(tree, console=console, auto_refresh=True, refresh_per_second=12) as live:
        run_extract(processor, tree)
        processor.save_all()
        live.refresh()
        
    processor.cleanup()
