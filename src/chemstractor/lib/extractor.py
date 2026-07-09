import time
import sys
import re
import os
import io
import logging
from functools import wraps
from contextlib import redirect_stdout, redirect_stderr, contextmanager

def capture_logs(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self._capture_logs():
            self.log_stream.write(f"Running: {func.__name__}\n")
            return func(self, *args, **kwargs)
    return wrapper


def time_function(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        elapsed = time.time() - start_time
        self.log_stream.write(f"Function {func.__name__} took {elapsed:.4f} seconds to execute.\n")
        return result
    return wrapper


def make_serializable(obj):
    from enum import Enum
    import dataclasses
    if isinstance(obj, Enum):
        return obj.value
    if hasattr(obj, "model_dump") and callable(obj.model_dump):
        return obj.model_dump()
    if hasattr(obj, "dict") and callable(obj.dict):
        return obj.dict()
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return str(obj)


_converter = None

def get_converter():
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter, PdfFormatOption
        from docling.datamodel.pipeline_options import ThreadedPdfPipelineOptions, RapidOcrOptions, PdfPipelineOptions
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
        from docling.datamodel.settings import settings
        import onnxruntime as ort
        import torch

        # Enable pipeline profiling timings
        settings.debug.profile_pipeline_timings = True

        # Determine the best accelerator device dynamically
        if torch.cuda.is_available():
            device = AcceleratorDevice.CUDA
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = AcceleratorDevice.MPS
        else:
            device = AcceleratorDevice.AUTO
            
        accelerator_options = AcceleratorOptions(device=device)

        # Define custom rapidocr parameters to ensure the execution providers are set correctly
        rapidocr_params = {}
        ocr_backend = "onnxruntime"
        
        # 1. Enable DirectML if available on Windows
        if "DmlExecutionProvider" in ort.get_available_providers():
            rapidocr_params["EngineConfig.onnxruntime.use_dml"] = True
            
        # 2. Enable CUDA if available
        if torch.cuda.is_available():
            if "CUDAExecutionProvider" in ort.get_available_providers():
                rapidocr_params["EngineConfig.onnxruntime.use_cuda"] = True
            else:
                # If CUDA is available but ONNX Runtime cannot use it (e.g. CPU-only ORT or mismatch),
                # fall back to using the 'torch' backend for OCR to run on the GPU via PyTorch
                ocr_backend = "torch"

        # 3. Check system RAM to prevent OOM crash due to formula enrichment model
        do_formula_enrichment = True
        try:
            import psutil
            total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)
            if total_ram_gb < 16.0:
                do_formula_enrichment = False
                sys.stderr.write(f"System RAM is {total_ram_gb:.1f} GB (below 16 GB threshold). Disabling formula enrichment to prevent Out-Of-Memory crashes.\n")
        except Exception as e:
            sys.stderr.write(f"Could not check system RAM: {e}. Defaulting to enabling formula enrichment.\n")

        if device not in (AcceleratorDevice.CUDA, AcceleratorDevice.MPS):
            # On CPU, using single-threaded PdfPipelineOptions is much more memory-efficient and avoids Windows multiprocessing crashes/deadlocks
            pipeline_options = PdfPipelineOptions(
                accelerator_options=accelerator_options,
                do_formula_enrichment=do_formula_enrichment,
            )
            # Force float32 precision for the formula model to avoid "addmm_impl_cpu_" Half precision error on CPU
            if do_formula_enrichment:
                for c in pipeline_options.code_formula_options.model_spec.engine_overrides.values():
                    if hasattr(c, "torch_dtype"):
                        c.torch_dtype = "float32"
                    if hasattr(c, "extra_config") and isinstance(c.extra_config, dict):
                        c.extra_config["torch_dtype"] = "float32"
        else:
            pipeline_options = ThreadedPdfPipelineOptions(
                accelerator_options=accelerator_options,
                do_formula_enrichment=do_formula_enrichment,
                ocr_batch_size=64,
                layout_batch_size=64,
                table_batch_size=4
            )
        
        if ocr_backend == "onnxruntime":
            pipeline_options.ocr_options = RapidOcrOptions(
                backend="onnxruntime",
                rapidocr_params=rapidocr_params
            )
        else:
            pipeline_options.ocr_options = RapidOcrOptions(
                backend="torch"
            )

        _converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
    return _converter


class TableExtractor:
    @staticmethod
    def clean_markdown(text: str) -> str:
        if not text:
            return ""
        # Remove XML control characters (ASCII 0-31 except tab (9), LF (10), CR (13), and surrogates/etc.)
        illegal_chars = re.compile(r'[\000-\010\013\014\016-\037\ufffe\uffff]')
        return illegal_chars.sub("", text)

    @property
    def logs(self) -> str:
        return self.log_stream.getvalue()

    def __init__(self):
        self.log_stream = io.StringIO()
        self._is_capturing = False
        
        self.input_path = None
        self.clean_pdf_bytes = None
        self._raw_result = None
        self._parsed_result = None
        self.raw_markdown = None
        self.parsed_markdown = None
        self.tables_markdown = []
        self.tables_csv = []
        self._is_parsed = False
        self.clean_path = None
        self.log_file_path = None

    def load_pdf(self, input_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input PDF path does not exist: {input_path}")
        if not os.path.isfile(input_path):
            raise ValueError(f"Input PDF path is not a file: {input_path}")
            
        self.input_path = os.path.abspath(input_path)
        self.clean_pdf_bytes = None
        self._raw_result = None
        self._parsed_result = None
        self.raw_markdown = None
        self.parsed_markdown = None
        self.tables_markdown = []
        self.tables_csv = []
        self._is_parsed = False
        self.clean_path = None
        self.log_file_path = None

    def load_extract_data(self, extract_dir: str):
        """Loads extract data from the filesystem into the extractor."""
        if not os.path.exists(extract_dir):
            raise FileNotFoundError(f"Extract directory does not exist: {extract_dir}")
            
        extract_dir = os.path.abspath(extract_dir)
        
        # Load clean pdf bytes
        self.clean_pdf_bytes = b""
        clean_files = [f for f in os.listdir(extract_dir) if f.startswith("clean_") and f.endswith(".pdf")]
        if clean_files:
            self.clean_path = os.path.join(extract_dir, clean_files[0])
            with open(self.clean_path, "rb") as f:
                self.clean_pdf_bytes = f.read()
                
        # Load parsed markdown (cleaned)
        self.parsed_markdown = ""
        clean_md_path = os.path.join(extract_dir, "output_clean.md")
        if os.path.exists(clean_md_path):
            with open(clean_md_path, "r", encoding="utf-8") as f:
                self.parsed_markdown = f.read()
        else:
            # Fallback to output.md for backward compatibility
            parsed_md_path = os.path.join(extract_dir, "output.md")
            if os.path.exists(parsed_md_path):
                with open(parsed_md_path, "r", encoding="utf-8") as f:
                    self.parsed_markdown = f.read()

        # Load raw markdown (unclean)
        self.raw_markdown = ""
        raw_md_path = os.path.join(extract_dir, "output.md")
        if os.path.exists(raw_md_path):
            with open(raw_md_path, "r", encoding="utf-8") as f:
                self.raw_markdown = f.read()
                
        # Load logs
        log_files = [f for f in os.listdir(extract_dir) if f.startswith("log_") and f.endswith(".log")]
        if log_files:
            self.log_file_path = os.path.join(extract_dir, log_files[0])
            with open(self.log_file_path, "r", encoding="utf-8") as f:
                logs_content = f.read()
                self.log_stream = io.StringIO(logs_content)
        else:
            self.log_stream = io.StringIO()
            
        # Load tables markdown and tables csv
        self.tables_markdown = []
        tables_dir = os.path.join(extract_dir, "tables")
        txt_dir = os.path.join(tables_dir, "txt")
        if os.path.exists(txt_dir):
            txt_files = [f for f in os.listdir(txt_dir) if f.startswith("table") and f.endswith(".txt")]
            def get_num(filename):
                match = re.search(r'\d+', filename)
                return int(match.group()) if match else 0
            txt_files.sort(key=get_num)
            for file_name in txt_files:
                file_path = os.path.join(txt_dir, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    self.tables_markdown.append(f.read())
                    
        self.tables_csv = []
        csv_dir = os.path.join(tables_dir, "csv")
        if os.path.exists(csv_dir):
            csv_files = [f for f in os.listdir(csv_dir) if f.startswith("table") and f.endswith(".csv")]
            def get_num(filename):
                match = re.search(r'\d+', filename)
                return int(match.group()) if match else 0
            csv_files.sort(key=get_num)
            for file_name in csv_files:
                file_path = os.path.join(csv_dir, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    self.tables_csv.append(f.read())
                    
        self._is_parsed = True

    @contextmanager
    def _capture_logs(self):
        if self._is_capturing:
            yield
            return
            
        self._is_capturing = True
        
        log_file = None
        if self.log_file_path:
            try:
                os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
                log_file = open(self.log_file_path, "a", encoding="utf-8", buffering=1)
            except Exception:
                pass

        class TeeStream:
            def __init__(self, string_io, file):
                self.string_io = string_io
                self.file = file

            def write(self, data):
                self.string_io.write(data)
                if self.file:
                    self.file.write(data)
                    self.file.flush()

            def flush(self):
                self.string_io.flush()
                if self.file:
                    self.file.flush()

            def getvalue(self):
                return self.string_io.getvalue()

        active_stream = TeeStream(self.log_stream, log_file) if log_file else self.log_stream
        
        old_log_stream = self.log_stream
        self.log_stream = active_stream
        
        try:
            with redirect_stdout(active_stream), redirect_stderr(active_stream):
                root_logger = logging.getLogger()
                temp_handler = logging.StreamHandler(active_stream)
                root_logger.addHandler(temp_handler)
                try:
                    yield
                finally:
                    root_logger.removeHandler(temp_handler)
        finally:
            self.log_stream = old_log_stream
            if log_file:
                log_file.close()
            self._is_capturing = False

    def clean_pdf(self):
        self.redact_hyperlinked_text()

    def redact_hyperlinked_text(self):
        import fitz  # PyMuPDF
        doc = fitz.open(self.input_path)
        for page in doc:
            # get_links() returns a list of dictionaries representing all clickable areas
            links = page.get_links()
            for link in links:
                # link["from"] contains the exact bounding box (fitz.Rect) of the hyperlink
                link_rect = link["from"]
                # Add a redaction annotation over this specific box, filled with white
                page.add_redact_annot(link_rect, fill=(1, 1, 1))
            # Apply the redactions, physically wiping the text under the boxes
            page.apply_redactions()
        # Save to in-memory bytes
        self.clean_pdf_bytes = doc.tobytes()
        doc.close()
        self.log_stream.write("All hyperlinked elements redacted in-memory.\n")

    @capture_logs
    @time_function
    def get_tables(self, doc_str: str) -> list[str]:
        blocks = doc_str.split('\n\n')
        table_strings = []
        for i, block in enumerate(blocks):
            # A standard Markdown table contains a header separator row like "|---"
            if '|---' in block or '| ---' in block:
                # Add the table itself
                table_strings.append(f"**[Table Data]**\n{block.strip()}")
        return table_strings

    @capture_logs
    @time_function
    def get_surrounding_paragraphs(self, num_context_paragraphs: int = 1) -> list[tuple[str, str]]:
        if not self.raw_markdown:
            return []
        blocks = self.raw_markdown.split('\n\n')
        surrounding_paragraphs = []
        for i, block in enumerate(blocks):
            # A standard Markdown table contains a header separator row like "|---"
            if '|---' in block or '| ---' in block:
                preceding_str = ""
                succeeding_str = ""
                
                # Grab paragraphs before the table (often the caption or introduction)
                preceding_paragraphs = []
                count = 0
                j = i - 1
                while j >= 0 and count < num_context_paragraphs:
                    prev_block = blocks[j].strip()
                    if prev_block:
                        if '|---' in prev_block or '| ---' in prev_block:
                            preceding_paragraphs.insert(0, "[table omitted]")
                        else:
                            preceding_paragraphs.insert(0, prev_block)
                            count += 1
                    j -= 1
                if preceding_paragraphs:
                    preceding_text = "\n\n".join(preceding_paragraphs)
                    preceding_str = f"**[Preceding Paragraphs]**\n{preceding_text}"
                
                # Grab paragraphs after the table (often table footnotes or continuation)
                succeeding_paragraphs = []
                count = 0
                j = i + 1
                while j < len(blocks) and count < num_context_paragraphs:
                    next_block = blocks[j].strip()
                    if next_block:
                        if '|---' in next_block or '| ---' in next_block:
                            succeeding_paragraphs.append("[table omitted]")
                        else:
                            succeeding_paragraphs.append(next_block)
                            count += 1
                    j += 1
                if succeeding_paragraphs:
                    succeeding_text = "\n\n".join(succeeding_paragraphs)
                    succeeding_str = f"**[Succeeding Paragraphs]**\n{succeeding_text}"

                surrounding_paragraphs.append((preceding_str, succeeding_str))
        return surrounding_paragraphs

    @capture_logs
    @time_function
    def parse_pdf(self):
        if self._is_parsed:
            return
            
        from docling.datamodel.base_models import DocumentStream
        import json
        
        converter = get_converter()
        
        # 1. Run conversion on raw input PDF to obtain context paragraphs
        self._raw_result = converter.convert(self.input_path)
        self.raw_markdown = self.clean_markdown(self._raw_result.document.export_to_markdown())
        if hasattr(self._raw_result, "timings") and self._raw_result.timings:
            self.log_stream.write(f"Raw PDF conversion timings:\n{json.dumps(self._raw_result.timings, default=make_serializable, indent=2)}\n")
        
        # 2. Redact the hyperlinked text in-memory
        self.clean_pdf()
        
        # 3. Convert the clean PDF from in-memory bytes
        filename = os.path.basename(self.input_path)
        stream = DocumentStream(name=f"clean_{filename}", stream=io.BytesIO(self.clean_pdf_bytes))
        self._parsed_result = converter.convert(stream)
        self.parsed_markdown = self.clean_markdown(self._parsed_result.document.export_to_markdown())
        if hasattr(self._parsed_result, "timings") and self._parsed_result.timings:
            self.log_stream.write(f"Clean PDF conversion timings:\n{json.dumps(self._parsed_result.timings, default=make_serializable, indent=2)}\n")
        
        self._is_parsed = True
    
    def extract_results(self):
        # Extract table markdown content
        tables = self.get_tables(self.parsed_markdown)
        surrounding_paragraphs = self.get_surrounding_paragraphs(num_context_paragraphs=4)
        
        self.tables_markdown = []
        for i, table_str in enumerate(tables):
            formatted_table = (
                f"-------------- TABLE {i + 1} EXTRACTION --------------\n"
                f"{surrounding_paragraphs[i][0]}\n\n"
                f"{table_str}\n\n"
                f"{surrounding_paragraphs[i][1]}"
            )
            self.tables_markdown.append(formatted_table)
            
        # Extract table CSV content
        self.tables_csv = []
        for table in self._parsed_result.document.tables:
            table_df = table.export_to_dataframe(doc=self._parsed_result.document)
            csv_str = self.clean_markdown(table_df.to_csv())
            self.tables_csv.append(csv_str)