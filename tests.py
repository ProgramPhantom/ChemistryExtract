import glob
import os
from datetime import datetime
from extractor import TableExtractor
from categorisation import categorise_table
import time

TEST_DIR = "./tests"
MATERIAL_DIR = "./tests/material"


def run_tests(categorise_tables: bool = True, model: str = "gemini"):
    # Find all test PDF files
    pdf_files = glob.glob(os.path.join(MATERIAL_DIR, "*.pdf"))
    print(f"--------- TESTING {len(pdf_files)} FILES ---------")
    
    # Generate timestamp run directory (filesystem-friendly format: YYYY-MM-DD_HH-MM-SS)
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(TEST_DIR, "runs", run_id)
    
    clean_dir = os.path.join(run_dir, "clean")
    output_dir = os.path.join(run_dir, "output")
    logs_dir = os.path.join(run_dir, "logs")
    
    os.makedirs(clean_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    for pdf_path in pdf_files:
        base_name = os.path.basename(pdf_path)
        base_no_ext = os.path.splitext(base_name)[0]
        
        # Configure output paths within the timestamped run directory
        test_output_dir = os.path.join(output_dir, base_no_ext)
        os.makedirs(test_output_dir, exist_ok=True)
        clean_path = os.path.join(clean_dir, f"clean+{base_name}")
        
        timer = time.time()
        print(f"Running test for '{base_name}'")
        
        # Instantiate extractor (runs path validation immediately)
        extractor = TableExtractor(pdf_path, clean_path)
        
        # Perform conversions and extractions
        tables_list, parsed_markdown, _ = extractor.extract_table_content_markdown()
        csv_tables, _ = extractor.extract_table_content_csv()
        
        # Save the entire parsed markdown to a file
        parsed_md_path = os.path.join(test_output_dir, "output.md")
        with open(parsed_md_path, "w", encoding="utf-8") as parsed_file:
            parsed_file.write(parsed_markdown)
        
        # Save each table string one by one to the test folder as table1, table2, etc.
        tables_dir = os.path.join(test_output_dir, "tables")
        os.makedirs(tables_dir, exist_ok=True)
        for i, table_str in enumerate(tables_list):
            table_file_path = os.path.join(tables_dir, f"table{i + 1}.txt")
            with open(table_file_path, "w", encoding="utf-8") as table_file:
                table_file.write(table_str)
            
            # Save corresponding CSV if available
            if i < len(csv_tables):
                csv_file_path = os.path.join(tables_dir, f"table{i + 1}.csv")
                with open(csv_file_path, "w", encoding="utf-8") as csv_file:
                    csv_file.write(csv_tables[i])
            
            if categorise_tables:
                res = categorise_table(table_file_path, model=model)
                if res.success:
                    status = "Contains" if res.contains_diffusion else "Does NOT contain"
                    print(f"  Table {i + 1} ({os.path.basename(table_file_path)}) [{model}]: {status} chemical diffusion coefficient data.")
                else:
                    print(f"  Table {i + 1} ({os.path.basename(table_file_path)}) [{model}]: Failed with error: {res.error}")
        
        # Save Captured conversion logs (stored in extractor.logs)
        log_file_path = os.path.join(logs_dir, f"log_{base_name}.log")
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_file.write(extractor.logs)

        elapsed_time = time.time() - timer
        print(f"Completed test for '{base_name}' in {elapsed_time:.2f} seconds")



if __name__ == "__main__":    
    run_tests(model="llama3.1", categorise_tables=False)