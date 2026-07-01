import os
import json
import csv
import gc
import time
from chemstractor.lib.extractor import TableExtractor
from chemstractor.lib.categorisation import categorise_table
from chemstractor.lib.summariser import summarise_table_conditions
from chemstractor.lib.metadata import extract_paper_metadata
from chemstractor.models import pricing_matrix


class PDFProcessor:
    def __init__(self, pdf_path: str, output_dir: str = ".", model: str = "gemini-2.5-flash"):
        self.pdf_path = pdf_path
        self.model = model
        
        self.base_name = os.path.basename(pdf_path)
        self.base_no_ext = os.path.splitext(self.base_name)[0]
        
        # Output paths derived from output_dir
        self.output_dir = os.path.join(output_dir, self.base_no_ext)
        self.extract_dir = os.path.join(self.output_dir, "extract")
        self.tables_dir = os.path.join(self.extract_dir, "tables")
        
        self.clean_path = os.path.join(self.extract_dir, f"clean_{self.base_name}")
        self.parsed_md_path = os.path.join(self.extract_dir, "output.md")
        self.log_file_path = os.path.join(self.extract_dir, f"log_{self.base_name}.log")
        
        self.categorisation_dir = os.path.join(self.output_dir, "categorisation")
        self.summary_dir = os.path.join(self.output_dir, "summary")
        self.summary_json_path = os.path.join(self.summary_dir, "summary.json")
        
        # State
        self.extractor = None
        self.cat_data_list = []
        self.summarisation_data_list = []
        self.num_tables = 0
        self.cat_results = []
        self.sum_results = []
        self.metadata_res = None


    def _log_error(self, message: str):
        """Appends an error message to the log file."""
        try:
            with open(self.log_file_path, "a", encoding="utf-8") as lf:
                lf.write(f"PROCESSOR ERROR: {message}\n")
        except Exception:
            pass

    def extract(self):
        """Extracts content in-memory and yields status messages."""
        start_time = time.time()
        yield {"status": "working", "message": "Extracting text & tables..."}
        
        self.extractor = TableExtractor(self.pdf_path)
        self.num_tables = len(self.extractor.tables_markdown)

        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Extracted text & tables",
            "elapsed_time": elapsed_time,
            "num_tables": self.num_tables
        }

    
    def categorise(self):
        """Categorises each table in-memory and yields status events."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before categorising tables.")
            
        start_time = time.time()
        yield {"status": "working", "message": "Categorising extracted tables..."}
        
        self.cat_results = []
        self.cat_data_list = []
        
        for i in range(self.num_tables):
            table_name = f"table{i + 1}.txt"
            
            yield {
                "status": "table_start",
                "table_idx": i,
                "table_name": table_name,
                "message": f"Categorising table {i + 1}/{self.num_tables}..."
            }
            
            table_text = self.extractor.tables_markdown[i]
            res = categorise_table(table_text, model=self.model)
            if res.success:
                status = "Contains" if res.contains_diffusion else "Does NOT contain"
                status_msg = f"{status} chemical diffusion coefficient data"
                self.cat_results.append((table_name, True, status_msg, res.usage_metadata))
                
                categorisation_data = {
                    "contains_scientific_data": res.contains_scientific_data,
                    "contains_diffusion_coeff": res.contains_diffusion_coeff,
                    "contains_polymer_diffusion_coeff": res.contains_polymer_diffusion_coeff,
                    "contains_diffusion": res.contains_diffusion
                }
                self.cat_data_list.append(categorisation_data)
                
                yield {
                    "status": "table_complete",
                    "table_idx": i,
                    "table_name": table_name,
                    "success": True,
                    "status_message": status_msg,
                    "usage_metadata": res.usage_metadata
                }
            else:
                status_msg = f"Failed: {res.error}"
                self.cat_results.append((table_name, False, status_msg, None))
                self.cat_data_list.append(None)
                yield {
                    "status": "table_complete",
                    "table_idx": i,
                    "table_name": table_name,
                    "success": False,
                    "status_message": status_msg,
                    "usage_metadata": None
                }
                
        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Categorised extracted tables",
            "elapsed_time": elapsed_time,
            "results": self.cat_results
        }


    def extract_metadata(self):
        """Extracts paper-level metadata and yields status events."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before extracting metadata.")
            
        start_time = time.time()
        yield {"status": "working", "message": "Extracting paper-level metadata..."}
        
        metadata_res = extract_paper_metadata(self.extractor.parsed_markdown, model=self.model)
        self.metadata_res = metadata_res
        
        metadata_error = None if metadata_res.success else metadata_res.error
        
        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Extracted paper-level metadata",
            "elapsed_time": elapsed_time,
            "success": metadata_res.success,
            "error": metadata_error,
            "usage_metadata": metadata_res.usage_metadata
        }


    def summarise(self):
        """Summarises each table in-memory and yields status events."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before summarising tables.")
            
        start_time = time.time()
        yield {"status": "working", "message": "Summarising tables..."}
        
        self.sum_results = []
        self.summarisation_data_list = []
        
        metadata_error = None
        if self.metadata_res and not self.metadata_res.success:
            metadata_error = self.metadata_res.error
            
        for i in range(self.num_tables):
            table_name = f"table{i + 1}.txt"
            
            yield {
                "status": "table_start",
                "table_idx": i,
                "table_name": table_name,
                "message": f"Summarising table {i + 1}/{self.num_tables}..."
            }
            
            table_text = self.extractor.tables_markdown[i]
            res = summarise_table_conditions(table_text, model=self.model)
            
            if res.success:
                # Store experimental conditions only
                self.summarisation_data_list.append(res.data.model_dump())
                
                status_msg = "Successfully summarised"
                if metadata_error:
                    status_msg += f" (metadata extraction failed: {metadata_error})"
                self.sum_results.append((table_name, True, status_msg, res.usage_metadata))
                
                yield {
                    "status": "table_complete",
                    "table_idx": i,
                    "table_name": table_name,
                    "success": True,
                    "status_message": status_msg,
                    "usage_metadata": res.usage_metadata
                }
            else:
                status_msg = f"Failed: {res.error}"
                self.sum_results.append((table_name, False, status_msg, None))
                self.summarisation_data_list.append(None)
                yield {
                    "status": "table_complete",
                    "table_idx": i,
                    "table_name": table_name,
                    "success": False,
                    "status_message": status_msg,
                    "usage_metadata": None
                }
                
        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Summarised experimental conditions",
            "elapsed_time": elapsed_time,
            "results": self.sum_results
        }

    def create_excel(self, dest_path: str = None) -> None:
        """Creates a beautifully formatted Excel document using the in-memory data of the processor."""
        from chemstractor.lib.report import create_excel
        
        # 1. Gather metadata
        metadata = {}
        if self.metadata_res and self.metadata_res.success:
            try:
                metadata = self.metadata_res.data.model_dump()
            except AttributeError:
                metadata = self.metadata_res.data if isinstance(self.metadata_res.data, dict) else {}
        
        # 2. Gather tables data
        tables_data = []
        for i in range(self.num_tables):
            table_data = {}
            if self.summarisation_data_list and i < len(self.summarisation_data_list):
                table_data = self.summarisation_data_list[i] or {}
                
            cat_data = {}
            if self.cat_data_list and i < len(self.cat_data_list):
                cat_data = self.cat_data_list[i] or {}
                
            csv_rows = None
            csv_error = None
            if self.extractor and self.extractor.tables_csv and i < len(self.extractor.tables_csv):
                csv_str = self.extractor.tables_csv[i]
                if csv_str:
                    try:
                        reader = csv.reader(csv_str.splitlines())
                        csv_rows = list(reader)
                    except Exception as e:
                        csv_error = str(e)
                        
            tables_data.append({
                "table_data": table_data,
                "cat_data": cat_data,
                "csv_rows": csv_rows,
                "csv_error": csv_error
            })
            
        # 3. Resolve destination path
        if dest_path is None:
            output_filename = f"{self.base_no_ext}_summary.xlsx"
            dest_path = os.path.join(self.summary_dir, output_filename)
            
        create_excel(
            dest_path=dest_path,
            base_no_ext=self.base_no_ext,
            metadata=metadata,
            tables_data=tables_data,
            log_error_fn=self._log_error
        )



    def save_logs(self):
        """Saves the extraction log file."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before saving logs.")
        with open(self.log_file_path, "w", encoding="utf-8") as log_file:
            log_file.write(self.extractor.logs)

    def save_cleaned_pdf(self):
        """Saves the cleaned PDF byte content to the specified path."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before saving cleaned PDF.")
        with open(self.clean_path, "wb") as clean_file:
            clean_file.write(self.extractor.clean_pdf_bytes)

    def save_summary_json(self):
        """Saves the paper metadata to the summary JSON file."""
        if self.metadata_res and self.metadata_res.success:
            os.makedirs(self.summary_dir, exist_ok=True)
            try:
                with open(self.summary_json_path, 'w', encoding='utf-8') as jf:
                    json.dump(self.metadata_res.data.model_dump(), jf, indent=2)
            except Exception as e:
                self._log_error(f"Error saving summary JSON {self.summary_json_path}: {e}")

    def save_outputs(self):
        """Saves the parsed markdown and extraction tables (text & csv)."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before saving outputs.")
            
        # Save parsed markdown
        with open(self.parsed_md_path, "w", encoding="utf-8") as parsed_file:
            parsed_file.write(self.extractor.parsed_markdown)
            
        # Save text tables
        txt_dir = os.path.join(self.tables_dir, "txt")
        os.makedirs(txt_dir, exist_ok=True)
        for i, table_str in enumerate(self.extractor.tables_markdown):
            table_file_path = os.path.join(txt_dir, f"table{i + 1}.txt")
            with open(table_file_path, "w", encoding="utf-8") as table_file:
                table_file.write(table_str)
                
        # Save CSV tables
        csv_dir = os.path.join(self.tables_dir, "csv")
        os.makedirs(csv_dir, exist_ok=True)
        for i, csv_str in enumerate(self.extractor.tables_csv):
            csv_file_path = os.path.join(csv_dir, f"table{i + 1}.csv")
            with open(csv_file_path, "w", encoding="utf-8") as csv_file:
                csv_file.write(csv_str)
                
        # Save paper metadata summary if available
        self.save_summary_json()

    def save_all(self):
        """Saves all relevant content in-memory to the output folder structure."""
        if not self.extractor:
            raise RuntimeError("Must call extract() before saving.")
        
        # Create output directories
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.extract_dir, exist_ok=True)
        os.makedirs(self.tables_dir, exist_ok=True)
        
        # 1. Save extraction files
        self.save_cleaned_pdf()
        self.save_outputs()
        self.save_logs()
        
        # 2. Save categorisation JSONs if available
        if self.cat_data_list:
            os.makedirs(self.categorisation_dir, exist_ok=True)
            for i, cat_data in enumerate(self.cat_data_list):
                if cat_data is not None:
                    json_file_path = os.path.join(self.categorisation_dir, f"table{i + 1}.json")
                    with open(json_file_path, 'w', encoding='utf-8') as jf:
                        json.dump(cat_data, jf, indent=2)
                        
        # 3. Save summarisation JSONs if available
        if self.summarisation_data_list:
            tables_summary_dir = os.path.join(self.summary_dir, "tables")
            os.makedirs(tables_summary_dir, exist_ok=True)
            for i, sum_data in enumerate(self.summarisation_data_list):
                if sum_data is not None:
                    json_file_path = os.path.join(tables_summary_dir, f"table{i + 1}.json")
                    with open(json_file_path, 'w', encoding='utf-8') as jf:
                        json.dump(sum_data, jf, indent=2)
                        
        self.save_summary_json()


    def cleanup(self):
        """Deload extractor instance and force garbage collection to release memory."""
        self.extractor = None
        gc.collect()
