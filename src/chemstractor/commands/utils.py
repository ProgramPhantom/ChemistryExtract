import os
import sys
import glob
import shutil
from datetime import datetime
from rich.console import Console

from chemstractor.lib.processor import PDFProcessor

def prepare_processor(
    pdf_path_or_dir: str,
    output_dir: str,
    model: str,
    direct: bool = False,
    same_folder: bool = True,
    suffix: str = "processed"
) -> tuple[PDFProcessor, str]:
    """Helper to initialize and load the PDFProcessor.
    
    If direct is True:
        - Validates that pdf_path_or_dir (which represents process_output_dir) contains extract/output.md.
        - Resolves output_dir. If same_folder is False, copies the extract directory
          to a new directory next to the input folder, named <input_folder>_<suffix>.
        - Instantiates PDFProcessor and loads it using load_output(output_dir).
    If direct is False:
        - Instantiates PDFProcessor and loads it using load_pdf(pdf_path, output_dir).
    """
    console = Console(file=sys.__stdout__)
    processor = PDFProcessor()

    if direct:
        process_output_dir = pdf_path_or_dir
        extract_dir = os.path.join(process_output_dir, "extract")
        if not os.path.isdir(extract_dir) or not os.path.isfile(os.path.join(extract_dir, "output.md")):
            console.print(f"[bold red]Error: The input folder '{process_output_dir}' must contain an 'extract' subfolder with extracted data.[/bold red]")
            sys.exit(1)

        if same_folder:
            resolved_output_dir = process_output_dir
        else:
            # Create a new output folder next to the input folder
            input_abs = os.path.abspath(os.path.normpath(process_output_dir))
            parent_dir = os.path.dirname(input_abs)
            base_name = os.path.basename(input_abs)
            new_dir = os.path.join(parent_dir, f"{base_name}_{suffix}")

            console.print(f"Creating new output folder and copying extract to: [yellow]{new_dir}[/yellow]")
            new_extract_dir = os.path.join(new_dir, "extract")
            os.makedirs(new_dir, exist_ok=True)
            if os.path.exists(new_extract_dir):
                shutil.rmtree(new_extract_dir)
            shutil.copytree(extract_dir, new_extract_dir)
            resolved_output_dir = new_dir

        processor.load_output(resolved_output_dir)
    else:
        resolved_output_dir = output_dir if output_dir is not None else "."
        processor.load_pdf(pdf_path_or_dir, resolved_output_dir)

    return processor, resolved_output_dir


def prepare_batch_dirs(
    pdf_dir: str,
    output_parent_dir: str,
    direct: bool = False
) -> tuple[str, str, list[str]]:
    """Helper to resolve and prepare directories for batch processing (process_all).
    
    If direct is True:
        - Resolves pdf_dir (input parent folder) to the most recent timestamped run if not specified.
        - Resolves output_parent_dir.
        - Scans pdf_dir for subdirectories containing 'extract/output.md'.
        - Setups a timestamped target directory inside output_parent_dir.
        - Copies each valid subdirectory's 'extract' folder to the new timestamped folder.
        - Returns (pdf_dir, run_dir, list of subfolder paths inside the new run_dir).
    If direct is False:
        - Resolves pdf_dir (default: ./tests/corpus).
        - Resolves output_parent_dir (default: ./tests/runs).
        - Setups a timestamped target directory inside output_parent_dir.
        - Returns (pdf_dir, run_dir, list of pdf file paths inside pdf_dir).
    """
    console = Console(file=sys.__stdout__)
    
    runs_parent = "./tests/runs"
    if not os.path.exists(runs_parent):
        runs_parent = "tests/runs"

    if direct:
        # Resolve pdf_dir (input_parent_dir): by default the most recent folder in tests/runs
        if pdf_dir is None:
            if os.path.exists(runs_parent):
                subdirs = [
                    d for d in os.listdir(runs_parent)
                    if os.path.isdir(os.path.join(runs_parent, d))
                ]
                if subdirs:
                    subdirs.sort()
                    pdf_dir = os.path.join(runs_parent, subdirs[-1])
                else:
                    console.print("[bold red]Error: No run folders found in tests/runs/ to use as input.[/bold red]")
                    sys.exit(1)
            else:
                console.print("[bold red]Error: tests/runs/ directory does not exist and no input path was provided.[/bold red]")
                sys.exit(1)
                
        if output_parent_dir is None:
            output_parent_dir = runs_parent

        if not os.path.exists(pdf_dir) or not os.path.isdir(pdf_dir):
            console.print(f"[bold red]Error: Input directory '{pdf_dir}' does not exist or is not a directory.[/bold red]")
            sys.exit(1)

        # Scan for subfolders containing an 'extract' folder with output.md
        subfolders = []
        for name in os.listdir(pdf_dir):
            path = os.path.join(pdf_dir, name)
            if os.path.isdir(path):
                extract_path = os.path.join(path, "extract")
                if os.path.isdir(extract_path) and os.path.isfile(os.path.join(extract_path, "output.md")):
                    subfolders.append(path)
                    
        if not subfolders:
            console.print(f"[bold red]Error: No folders containing pre-extracted data (an 'extract' subfolder with output.md) were found in '{pdf_dir}'.[/bold red]")
            sys.exit(1)
            
        # Setup timestamped run directory
        run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        run_dir = os.path.join(output_parent_dir, run_id)
        os.makedirs(run_dir, exist_ok=True)
        
        target_dirs = []
        for src_subdir_path in subfolders:
            base_name = os.path.basename(src_subdir_path)
            dest_subdir_path = os.path.join(run_dir, base_name)
            
            # Copy extract folder as-is
            src_extract = os.path.join(src_subdir_path, "extract")
            dest_extract = os.path.join(dest_subdir_path, "extract")
            os.makedirs(dest_subdir_path, exist_ok=True)
            shutil.copytree(src_extract, dest_extract)
            
            target_dirs.append(dest_subdir_path)
            
        return pdf_dir, run_dir, target_dirs

    else:
        if pdf_dir is None:
            pdf_dir = "./tests/corpus"
        if output_parent_dir is None:
            output_parent_dir = "./tests/runs"
            
        # Scan for PDF files in the corpus directory
        pdf_pattern = os.path.join(pdf_dir, "*.pdf")
        pdf_files = glob.glob(pdf_pattern)
        
        if not pdf_files:
            console.print(f"[bold red]Error: No PDF files found in {pdf_dir}[/bold red]")
            sys.exit(1)
            
        # Setup timestamped run directory
        run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        run_dir = os.path.join(output_parent_dir, run_id)
        os.makedirs(run_dir, exist_ok=True)
        
        return pdf_dir, run_dir, pdf_files
