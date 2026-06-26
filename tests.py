import glob
import os
from datetime import datetime
from extractor import TableExtractor
from categorisation import categorise_table
import time
import gc

TEST_DIR = "./tests"
MATERIAL_DIR = "./tests/material"


def setup_run_layout(test_dir: str) -> tuple[str, str, str]:
    """Creates the timestamped directories for the run and returns their paths."""
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(test_dir, "runs", run_id)
    
    clean_dir = os.path.join(run_dir, "clean")
    output_dir = os.path.join(run_dir, "output")
    logs_dir = os.path.join(run_dir, "logs")
    
    os.makedirs(clean_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    return clean_dir, output_dir, logs_dir


def save_cleaned_pdf(clean_path: str, clean_pdf_bytes: bytes):
    """Saves the cleaned PDF byte content to the specified path."""
    with open(clean_path, "wb") as clean_file:
        clean_file.write(clean_pdf_bytes)


def save_parsed_markdown(parsed_md_path: str, parsed_markdown: str):
    """Saves the entire parsed markdown to the specified path."""
    with open(parsed_md_path, "w", encoding="utf-8") as parsed_file:
        parsed_file.write(parsed_markdown)


def save_tables_text(tables_dir: str, tables_list: list[str]):
    """Saves each extracted table string to table1.txt, table2.txt, etc. in tables_dir."""
    os.makedirs(tables_dir, exist_ok=True)
    for i, table_str in enumerate(tables_list):
        table_file_path = os.path.join(tables_dir, f"table{i + 1}.txt")
        with open(table_file_path, "w", encoding="utf-8") as table_file:
            table_file.write(table_str)


def save_tables_csv(tables_dir: str, csv_tables: list[str]):
    """Saves each extracted table CSV string to table1.csv, table2.csv, etc. in tables_dir."""
    os.makedirs(tables_dir, exist_ok=True)
    for i, csv_str in enumerate(csv_tables):
        csv_file_path = os.path.join(tables_dir, f"table{i + 1}.csv")
        with open(csv_file_path, "w", encoding="utf-8") as csv_file:
            csv_file.write(csv_str)


def categorise_extracted_tables(tables_dir: str, num_tables: int, model: str):
    """Categorises each saved table text file and logs results."""
    for i in range(num_tables):
        table_file_path = os.path.join(tables_dir, f"table{i + 1}.txt")
        if os.path.exists(table_file_path):
            res = categorise_table(table_file_path, model=model)
            if res.success:
                status = "Contains" if res.contains_diffusion else "Does NOT contain"
                print(f"  Table {i + 1} ({os.path.basename(table_file_path)}) [{model}]: {status} chemical diffusion coefficient data.")
            else:
                print(f"  Table {i + 1} ({os.path.basename(table_file_path)}) [{model}]: Failed with error: {res.error}")


def save_logs(logs_dir: str, base_name: str, logs_content: str):
    """Saves the extraction log file."""
    log_file_path = os.path.join(logs_dir, f"log_{base_name}.log")
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        log_file.write(logs_content)


def run_tests(categorise_tables: bool = True, model: str = "gemini"):
    # Find all test PDF files
    pdf_files = glob.glob(os.path.join(MATERIAL_DIR, "*.pdf"))
    print(f"--------- TESTING {len(pdf_files)} FILES ---------")
    
    # 1. Setup timestamped run directories
    clean_dir, output_dir, logs_dir = setup_run_layout(TEST_DIR)
    
    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path)
        base_no_ext = os.path.splitext(base_name)[0]
        
        # Configure output paths within the timestamped run directory
        test_output_dir = os.path.join(output_dir, base_no_ext)
        os.makedirs(test_output_dir, exist_ok=True)
        clean_path = os.path.join(clean_dir, f"clean_{base_name}")
        
        timer = time.time()
        print(f"Running test for '{base_name}'")
        
        # 2. Extract content in-memory
        extractor = TableExtractor(pdf_path)
        
        # 3. Save Cleaned PDF
        save_cleaned_pdf(clean_path, extractor.clean_pdf_bytes)
        
        # 4. Save Extraction Outputs (Markdown, Tables, CSVs)
        parsed_md_path = os.path.join(test_output_dir, "output.md")
        save_parsed_markdown(parsed_md_path, extractor.parsed_markdown)
        
        tables_dir = os.path.join(test_output_dir, "tables")
        save_tables_text(tables_dir, extractor.tables_markdown)
        save_tables_csv(tables_dir, extractor.tables_csv)
        
        # 5. Run Categorisation if enabled
        if categorise_tables:
            categorise_extracted_tables(tables_dir, len(extractor.tables_markdown), model)
        
        # 6. Save Logs
        save_logs(logs_dir, base_name, extractor.logs)
        
        elapsed_time = time.time() - timer
        print(f"Completed test for '{base_name}' in {elapsed_time:.2f} seconds")

        # 7. Deload extractor instance to release memory
        extractor = None
        gc.collect()


if __name__ == "__main__":    
    run_tests(model="llama3.1", categorise_tables=False)