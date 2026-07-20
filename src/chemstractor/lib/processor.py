import os
import json
import csv
import gc
import time
from chemstractor.lib.extractor import TableExtractor
from chemstractor.lib.categoriser import categorise_table
from chemstractor.lib.summariser import summarise_table_conditions
from chemstractor.lib.metadata import extract_paper_metadata
from chemstractor.lib.interpreter import interpret_table


class MetadataResult:
    def __init__(self, success: bool, data: dict, error: str = None, usage_metadata: dict = None):
        self.success = success
        self.data = data
        self.error = error
        self.usage_metadata = usage_metadata


class PDFProcessor:
    def __init__(self):
        self.pdf_path = None
        self.base_name = None
        self.base_no_ext = None
        
        self.output_dir = None
        self.extract_dir = None
        self.tables_dir = None
        
        self.clean_path = None
        self.parsed_md_path = None
        self.clean_md_path = None
        self.log_file_path = None
        self.categorisation_dir = None
        self.summary_dir = None
        self.summary_json_path = None
        self.interpretation_dir = None
        self.interpretation_data_list = []
        self.interpret_results = []
        
        # State
        self.extractor = None
        self.cat_data_list = []
        self.summarisation_data_list = []
        self.num_tables = 0
        self.cat_results = []
        self.sum_results = []
        self.metadata_res = None
        self.tables_csv_rows = []
        self.command_outputs = {}

    def load_pdf(self, pdf_path: str, output_dir: str = "."):
        """Initializes paths and fields for processing a specific PDF."""
        self.pdf_path = pdf_path
        self.base_name = os.path.basename(pdf_path)
        self.base_no_ext = os.path.splitext(self.base_name)[0]
        
        self.output_dir = os.path.join(output_dir, self.base_no_ext)
        self.extract_dir = os.path.join(self.output_dir, "extract")
        self.tables_dir = os.path.join(self.extract_dir, "tables")
        
        self.clean_path = os.path.join(self.extract_dir, f"clean_{self.base_name}")
        self.parsed_md_path = os.path.join(self.extract_dir, "output.md")
        self.clean_md_path = os.path.join(self.extract_dir, "output_clean.md")
        self.log_file_path = os.path.join(self.extract_dir, f"log_{self.base_name}.log")
        self.categorisation_dir = os.path.join(self.output_dir, "categorisation")
        self.summary_dir = os.path.join(self.output_dir, "summary")
        self.summary_json_path = os.path.join(self.summary_dir, "summary.json")
        self.interpretation_dir = os.path.join(self.output_dir, "interpretation")
        self.interpretation_data_list = []
        self.interpret_results = []
        
        self.extractor = None
        self.cat_data_list = []
        self.summarisation_data_list = []
        self.num_tables = 0
        self.cat_results = []
        self.sum_results = []
        self.metadata_res = None
        self.tables_csv_rows = []
        self.command_outputs = {}

    def load_output(self, process_output_dir: str):
        """Loads all present command outputs from a process output folder."""
        self.output_dir = os.path.abspath(process_output_dir)
        self.base_no_ext = os.path.basename(os.path.normpath(self.output_dir))
        self.base_name = f"{self.base_no_ext}.pdf"
        
        self.extract_dir = os.path.join(self.output_dir, "extract")
        self.tables_dir = os.path.join(self.extract_dir, "tables")
        
        self.clean_path = os.path.join(self.extract_dir, f"clean_{self.base_name}")
        self.parsed_md_path = os.path.join(self.extract_dir, "output.md")
        self.clean_md_path = os.path.join(self.extract_dir, "output_clean.md")
        self.log_file_path = os.path.join(self.extract_dir, f"log_{self.base_name}.log")
        
        self.categorisation_dir = os.path.join(self.output_dir, "categorisation")
        self.summary_dir = os.path.join(self.output_dir, "summary")
        self.summary_json_path = os.path.join(self.summary_dir, "summary.json")
        self.interpretation_dir = os.path.join(self.output_dir, "interpretation")
        self.interpretation_data_list = []
        self.interpret_results = []
        
        # State initialization
        self.extractor = None
        self.cat_data_list = []
        self.summarisation_data_list = []
        self.num_tables = 0
        self.cat_results = []
        self.sum_results = []
        self.metadata_res = None
        self.tables_csv_rows = []
        
        # Storage for all present command outputs
        self.command_outputs = {
            "metadata": None,
            "categorisation": [],
            "summary_tables": [],
            "tables_csv": [],
            "tables_txt": [],
            "interpretation": []
        }
        
        # 1. Load Extract Data
        if os.path.exists(self.extract_dir):
            try:
                self.load_extract_data()
            except Exception as e:
                self._log_error(f"Error loading extract data in load_output: {e}")
        
        # 2. Load Metadata
        if os.path.exists(self.summary_json_path):
            try:
                with open(self.summary_json_path, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    self.command_outputs["metadata"] = metadata
                    self.metadata_res = MetadataResult(success=True, data=metadata)
            except Exception as e:
                self._log_error(f"Error loading metadata from {self.summary_json_path}: {e}")
                
        # 3. Scan and Gather Tables
        csv_dir = os.path.join(self.tables_dir, "csv")
        txt_dir = os.path.join(self.tables_dir, "txt")
        
        num_tables = self.num_tables
        if num_tables == 0:
            if os.path.exists(csv_dir):
                while os.path.exists(os.path.join(csv_dir, f"table{num_tables + 1}.csv")):
                    num_tables += 1
            elif os.path.exists(txt_dir):
                while os.path.exists(os.path.join(txt_dir, f"table{num_tables + 1}.txt")):
                    num_tables += 1
            self.num_tables = num_tables
        
        
        # 3. Load all present tables data
        for i in range(num_tables):
            # Categorisation
            cat_path = os.path.join(self.categorisation_dir, f"table{i + 1}.json")
            cat_data = None
            if os.path.exists(cat_path):
                try:
                    with open(cat_path, 'r', encoding='utf-8') as f:
                        cat_data = json.load(f)
                except Exception as e:
                    self._log_error(f"Error loading categorisation JSON {cat_path}: {e}")
            self.cat_data_list.append(cat_data)
            self.command_outputs["categorisation"].append(cat_data)
            
            # Summarisation
            sum_path = os.path.join(self.summary_dir, "tables", f"table{i + 1}.json")
            sum_data = None
            if os.path.exists(sum_path):
                try:
                    with open(sum_path, 'r', encoding='utf-8') as f:
                        sum_data = json.load(f)
                except Exception as e:
                    self._log_error(f"Error loading summary JSON {sum_path}: {e}")
            self.summarisation_data_list.append(sum_data)
            self.command_outputs["summary_tables"].append(sum_data)
            
            # CSV Rows
            csv_path = os.path.join(csv_dir, f"table{i + 1}.csv")
            csv_rows = None
            if os.path.exists(csv_path):
                try:
                    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
                        reader = csv.reader(f)
                        csv_rows = list(reader)
                except Exception as e:
                    self._log_error(f"Error loading CSV {csv_path}: {e}")
            self.tables_csv_rows.append(csv_rows)
            self.command_outputs["tables_csv"].append(csv_rows)
            
            # Text tables
            txt_path = os.path.join(txt_dir, f"table{i + 1}.txt")
            txt_content = None
            if os.path.exists(txt_path):
                try:
                    with open(txt_path, 'r', encoding='utf-8') as f:
                        txt_content = f.read()
                except Exception as e:
                    self._log_error(f"Error loading text table {txt_path}: {e}")
            self.command_outputs["tables_txt"].append(txt_content)
            
            # Interpretation
            interp_path = os.path.join(self.interpretation_dir, f"table{i + 1}.json")
            interp_data = None
            if os.path.exists(interp_path):
                try:
                    with open(interp_path, 'r', encoding='utf-8') as f:
                        interp_data = json.load(f)
                except Exception as e:
                    self._log_error(f"Error loading interpretation JSON {interp_path}: {e}")
            self.interpretation_data_list.append(interp_data)
            self.command_outputs["interpretation"].append(interp_data)


    def load_extract_data(self):
        """Loads extract data from the filesystem into the TableExtractor."""
        self.extractor = TableExtractor()
        self.extractor.load_extract_data(self.extract_dir)
        self.num_tables = len(self.extractor.tables_markdown)
        
        # Sync the paths in PDFProcessor with what was actually loaded
        if self.extractor.clean_path:
            self.clean_path = self.extractor.clean_path
        if self.extractor.log_file_path:
            self.log_file_path = self.extractor.log_file_path




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
        
        try:
            self.extractor = TableExtractor()
            self.extractor.load_pdf(self.pdf_path)
            self.extractor.log_file_path = self.log_file_path
            self.extractor.parse_pdf()
            self.extractor.extract_results()
            self.num_tables = len(self.extractor.tables_markdown)
        except MemoryError as e:
            self._log_error(f"Error in extract (MemoryError): {e}")
            logs = self.extractor.logs if (self.extractor and hasattr(self.extractor, 'logs')) else ""
            msg = (
                "Extraction failed: Out of Memory (MemoryError). The system has run out of RAM during document processing. "
                "Please close other applications to free up RAM, increase swap space, or use a system with more memory."
            )
            yield {
                "status": "error",
                "message": msg,
                "error": e,
                "logs": logs
            }
            return
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in extract: {e}")
            logs = self.extractor.logs if (self.extractor and hasattr(self.extractor, 'logs')) else ""
            yield {
                "status": "error",
                "message": f"Extraction failed: {str(e)}",
                "error": e,
                "logs": logs
            }
            return

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
            yield {
                "status": "complete",
                "message": "Categorisation skipped: extraction failed or was not run.",
                "elapsed_time": 0.0,
                "results": []
            }
            return
            
        start_time = time.time()
        yield {"status": "working", "message": "Categorising extracted tables..."}
        
        self.cat_results = []
        self.cat_data_list = []
        
        # Get title and abstract data if present. 
        title = None
        abstract = None
        if self.metadata_res and self.metadata_res.success and self.metadata_res.data:
            if hasattr(self.metadata_res.data, "model_dump"):
                meta_dict = self.metadata_res.data.model_dump()
            elif isinstance(self.metadata_res.data, dict):
                meta_dict = self.metadata_res.data
            else:
                meta_dict = {}
            title = meta_dict.get("title")
            abstract = meta_dict.get("abstract")
        
        try:
            for i in range(self.num_tables):
                table_name = f"table{i + 1}.txt"
                
                yield {
                    "status": "table_start",
                    "table_idx": i,
                    "table_name": table_name,
                    "message": f"Categorising table {i + 1}/{self.num_tables}..."
                }
                
                table_text = self.extractor.tables_markdown[i]
                res = categorise_table(table_text, title=title, abstract=abstract)
                if res.success:
                    if res.flagged:
                        flags = []
                        if res.contains_raw_diffusion_data:
                            flags.append("raw")
                        if res.contains_mark_houwink_parameters:
                            flags.append("mark_houwink")
                        if res.contains_flory_parameters:
                            flags.append("flory")
                        status_msg = ", ".join(flags) if flags else "flagged"
                    else:
                        status_msg = "Not flagged"
                    self.cat_results.append((table_name, True, status_msg, res.usage_metadata))
                    
                    categorisation_data = {
                        "contains_scientific_data": res.contains_scientific_data,
                        "contains_raw_diffusion_data": res.contains_raw_diffusion_data,
                        "contains_mark_houwink_parameters": res.contains_mark_houwink_parameters,
                        "contains_flory_parameters": res.contains_flory_parameters,
                        "contains_polymer_diffusion_coeff": res.contains_polymer_diffusion_coeff
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
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in categorise: {e}")
            elapsed_time = time.time() - start_time
            yield {
                "status": "complete",
                "message": f"Categorisation failed: {str(e)}",
                "elapsed_time": elapsed_time,
                "results": self.cat_results
            }
            return

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
            yield {
                "status": "complete",
                "message": "Metadata extraction skipped: extraction failed or was not run.",
                "elapsed_time": 0.0,
                "success": False,
                "error": "extraction failed",
                "usage_metadata": None
            }
            return
            
        start_time = time.time()
        yield {"status": "working", "message": "Extracting paper-level metadata..."}
        
        try:
            input_markdown = self.extractor.raw_markdown or self.extractor.parsed_markdown
            metadata_res = extract_paper_metadata(input_markdown)
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
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in extract_metadata: {e}")
            elapsed_time = time.time() - start_time
            self.metadata_res = MetadataResult(success=False, data={}, error=str(e))
            yield {
                "status": "complete",
                "message": f"Paper metadata extraction failed: {str(e)}",
                "elapsed_time": elapsed_time,
                "success": False,
                "error": str(e),
                "usage_metadata": None
            }


    def summarise(self):
        """Summarises each table in-memory and yields status events."""
        if not self.extractor:
            yield {
                "status": "complete",
                "message": "Summarisation skipped: extraction failed or was not run.",
                "elapsed_time": 0.0,
                "results": []
            }
            return
            
        start_time = time.time()
        yield {"status": "working", "message": "Summarising tables..."}
        
        self.sum_results = []
        self.summarisation_data_list = []
        
        metadata_error = None
        if self.metadata_res and not self.metadata_res.success:
            metadata_error = self.metadata_res.error
            
        try:
            for i in range(self.num_tables):
                table_name = f"table{i + 1}.txt"
                
                yield {
                    "status": "table_start",
                    "table_idx": i,
                    "table_name": table_name,
                    "message": f"Summarising table {i + 1}/{self.num_tables}..."
                }
                
                table_text = self.extractor.tables_markdown[i]
                res = summarise_table_conditions(table_text)
                
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
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in summarise: {e}")
            elapsed_time = time.time() - start_time
            yield {
                "status": "complete",
                "message": f"Summarisation failed: {str(e)}",
                "elapsed_time": elapsed_time,
                "results": self.sum_results
            }
            return
                
        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Summarised experimental conditions",
            "elapsed_time": elapsed_time,
            "results": self.sum_results
        }

    def interpret(self):
        """Interprets each table categorized as 'coeff' in-memory and yields status events."""
        if not self.extractor:
            yield {
                "status": "complete",
                "message": "Interpretation skipped: extraction failed or was not run.",
                "elapsed_time": 0.0,
                "results": []
            }
            return
            
        # Check if categorisation data is available
        categorised_count = sum(1 for c in self.cat_data_list if c is not None)
        if categorised_count == 0:
            yield {
                "status": "complete",
                "message": "Interpretation skipped: no table categorisation data found.",
                "elapsed_time": 0.0,
                "results": []
            }
            return
            
        start_time = time.time()
        yield {"status": "working", "message": "Interpreting 'coeff' tables..."}
        
        self.interpret_results = []
        self.interpretation_data_list = []
        
        title = None
        abstract = None
        if self.metadata_res and self.metadata_res.success and self.metadata_res.data:
            if hasattr(self.metadata_res.data, "model_dump"):
                meta_dict = self.metadata_res.data.model_dump()
            elif isinstance(self.metadata_res.data, dict):
                meta_dict = self.metadata_res.data
            else:
                meta_dict = {}
            title = meta_dict.get("title")
            abstract = meta_dict.get("abstract")
            
        try:
            for i in range(self.num_tables):
                table_name = f"table{i + 1}.txt"
                
                # Check if this table has categorisation "coeff"
                cat_data = self.cat_data_list[i] if i < len(self.cat_data_list) else None
                is_coeff = cat_data and (
                    cat_data.get("contains_scientific_data", False) and
                    cat_data.get("contains_polymer_diffusion_coeff", False) and (
                        cat_data.get("contains_mark_houwink_parameters", False) or
                        cat_data.get("contains_flory_parameters", False)
                    )
                )
                
                if not is_coeff:
                    # Skip tables that are not "coeff"
                    self.interpret_results.append((table_name, True, "Skipped (not coeff)", None, []))
                    self.interpretation_data_list.append(None)
                    continue
                    
                yield {
                    "status": "table_start",
                    "table_idx": i,
                    "table_name": table_name,
                    "message": f"Interpreting table {i + 1}/{self.num_tables}..."
                }
                
                table_text = self.extractor.tables_markdown[i]
                formulae = self.extractor.formulae if hasattr(self.extractor, 'formulae') else []
                res = interpret_table(table_text, title=title, abstract=abstract, cat_data=cat_data, formulae=formulae)
                
                if res.success:
                    data_dict = res.data.model_dump()
                    data_dict["calculator_calls"] = res.calculator_calls
                    
                    self.interpretation_data_list.append(data_dict)
                    status_msg = "Successfully interpreted"
                    self.interpret_results.append((table_name, True, status_msg, res.usage_metadata, res.calculator_calls))
                    
                    yield {
                        "status": "table_complete",
                        "table_idx": i,
                        "table_name": table_name,
                        "success": True,
                        "status_message": status_msg,
                        "usage_metadata": res.usage_metadata,
                        "calculator_calls": res.calculator_calls
                    }
                else:
                    status_msg = f"Failed: {res.error}"
                    self.interpret_results.append((table_name, False, status_msg, None, res.calculator_calls))
                    self.interpretation_data_list.append(None)
                    
                    yield {
                        "status": "table_complete",
                        "table_idx": i,
                        "table_name": table_name,
                        "success": False,
                        "status_message": status_msg,
                        "usage_metadata": None,
                        "calculator_calls": res.calculator_calls
                    }
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in interpret: {e}")
            elapsed_time = time.time() - start_time
            yield {
                "status": "complete",
                "message": f"Interpretation failed: {str(e)}",
                "elapsed_time": elapsed_time,
                "results": self.interpret_results
            }
            return
                
        elapsed_time = time.time() - start_time
        yield {
            "status": "complete",
            "message": "Interpreted coeff tables",
            "elapsed_time": elapsed_time,
            "results": self.interpret_results
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
            if self.tables_csv_rows and i < len(self.tables_csv_rows):
                csv_rows = self.tables_csv_rows[i]
            elif self.extractor and self.extractor.tables_csv and i < len(self.extractor.tables_csv):
                csv_str = self.extractor.tables_csv[i]
                if csv_str:
                    try:
                        reader = csv.reader(csv_str.splitlines())
                        csv_rows = list(reader)
                    except Exception as e:
                        csv_error = str(e)
                        
            interp_data = None
            if self.interpretation_data_list and i < len(self.interpretation_data_list):
                interp_data = self.interpretation_data_list[i] or {}

            tables_data.append({
                "table_data": table_data,
                "cat_data": cat_data,
                "csv_rows": csv_rows,
                "csv_error": csv_error,
                "interpretation": interp_data
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

    def save_pdf_copy(self):
        """Saves a copy of the original processed PDF to the output directory."""
        if not self.pdf_path or not os.path.exists(self.pdf_path):
            return
        dest = os.path.join(self.output_dir, self.base_name)
        import shutil
        shutil.copy2(self.pdf_path, dest)

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
            
        # Save parsed markdown (cleaned)
        with open(self.clean_md_path, "w", encoding="utf-8") as clean_file:
            clean_file.write(self.extractor.parsed_markdown)
            
        # Save raw/unclean markdown
        with open(self.parsed_md_path, "w", encoding="utf-8") as raw_file:
            raw_file.write(self.extractor.raw_markdown or "")
            
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
                
        # Save formulae json
        formulae_path = os.path.join(self.extract_dir, "formulae.json")
        try:
            with open(formulae_path, "w", encoding="utf-8") as f:
                json.dump(self.extractor.formulae, f, indent=2)
        except Exception as e:
            self._log_error(f"Error saving formulae JSON {formulae_path}: {e}")
                
        # Save paper metadata summary if available
        self.save_summary_json()

    def save_all(self):
        """Saves all relevant content in-memory to the output folder structure."""
        if not self.extractor:
            self._log_error("save_all skipped: no extractor available (extraction failed or was not run).")
            return
        
        try:
            # Create output directories
            os.makedirs(self.output_dir, exist_ok=True)
            os.makedirs(self.extract_dir, exist_ok=True)
            os.makedirs(self.tables_dir, exist_ok=True)
            
            # 1. Save extraction files
            self.save_cleaned_pdf()
            self.save_pdf_copy()
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
                            
            # 4. Save interpretation JSONs if available
            if self.interpretation_data_list:
                os.makedirs(self.interpretation_dir, exist_ok=True)
                for i, interp_data in enumerate(self.interpretation_data_list):
                    if interp_data is not None:
                        json_file_path = os.path.join(self.interpretation_dir, f"table{i + 1}.json")
                        with open(json_file_path, 'w', encoding='utf-8') as jf:
                            json.dump(interp_data, jf, indent=2)
                            
            self.save_summary_json()
        except BaseException as e:
            if isinstance(e, (KeyboardInterrupt, SystemExit)):
                raise e
            self._log_error(f"Error in save_all: {e}")

    def cleanup(self):
        """Deload extractor instance and force garbage collection to release memory."""
        self.extractor = None
        gc.collect()

