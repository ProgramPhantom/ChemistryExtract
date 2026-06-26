from docling.document_converter import DocumentConverter
import pandas as pd
import fitz  # PyMuPDF
import os
import glob
from datetime import datetime
import logging
from contextlib import redirect_stdout, redirect_stderr, contextmanager
import io
from functools import wraps
import time

_converter = DocumentConverter()

def capture_logs(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self._capture_logs():
            print(f"Running: {func.__name__}")
            return func(self, *args, **kwargs)
    return wrapper


def time_function(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Function {func.__name__} took {elapsed:.4f} seconds to execute.")
        return result
    return wrapper


def require_parsed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not getattr(self, "_is_parsed", False):
            print(f"Error: Cannot execute {func.__name__}. PDF parsing has not been executed.")
            return None
        return func(self, *args, **kwargs)
    return wrapper


class TableExtractor:
    _is_capturing = False
    log_stream = io.StringIO()

    @property
    def logs(self) -> str:
        return self.log_stream.getvalue()

    def __init__(self, input_path: str, output_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input PDF path does not exist: {input_path}")
        if not os.path.isfile(input_path):
            raise ValueError(f"Input PDF path is not a file: {input_path}")
            
        self.input_path = os.path.abspath(input_path)
        
        # Resolve output path dynamically
        filename = os.path.basename(self.input_path)
        if output_path.lower().endswith('.pdf'):
            self.output_path = os.path.abspath(output_path)
        else:
            self.output_path = os.path.abspath(os.path.join(output_path, f"clean_{filename}"))
            
        self._raw_result = None
        self._parsed_result = None
        self.raw_markdown = None
        self.parsed_markdown = None
        self._is_parsed = False
        
        # Parse PDF immediately upon instantiation
        self.parse_pdf()

    @contextmanager
    def _capture_logs(self):
        if self._is_capturing:
            yield
            return
            
        self._is_capturing = True
        with redirect_stdout(self.log_stream), redirect_stderr(self.log_stream):
            root_logger = logging.getLogger()
            temp_handler = logging.StreamHandler(self.log_stream)
            root_logger.addHandler(temp_handler)
            try:
                yield
            finally:
                root_logger.removeHandler(temp_handler)
                self._is_capturing = False

    def clean_pdf(self, input_path, output_path):
        self.redact_hyperlinked_text(input_path, output_path)

    def redact_hyperlinked_text(self, input_path, output_path):
        doc = fitz.open(input_path)
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
        doc.save(output_path)
        doc.close()
        print("All hyperlinked elements redacted. Clean PDF saved.")

    def get_tables(self, doc_str: str) -> list[str]:
        blocks = doc_str.split('\n\n')
        table_strings = []
        for i, block in enumerate(blocks):
            # A standard Markdown table contains a header separator row like "|---"
            if '|---' in block or '| ---' in block:
                # Add the table itself
                table_strings.append(f"**[Table Data]**\n{block.strip()}")
        return table_strings

    def get_surrounding_paragraphs(self, doc_str: str, num_context_paragraphs: int = 1) -> list[tuple[str, str]]:
        blocks = doc_str.split('\n\n')
        surrounding_paragraphs = []
        for i, block in enumerate(blocks):
            # A standard Markdown table contains a header separator row like "|---"
            if '|---' in block or '| ---' in block:
                preceding_str = ""
                succeeding_str = ""
                
                # Grab paragraphs before the table (often the caption or introduction)
                preceding_paragraphs = []
                for j in range(1, num_context_paragraphs + 1):
                    if i - j >= 0:
                        prev_block = blocks[i - j].strip()
                        if prev_block:
                            preceding_paragraphs.insert(0, prev_block)
                if preceding_paragraphs:
                    preceding_text = "\n\n".join(preceding_paragraphs)
                    preceding_str = f"**[Preceding Paragraphs]**\n{preceding_text}"
                
                # Grab paragraphs after the table (often table footnotes or continuation)
                succeeding_paragraphs = []
                for j in range(1, num_context_paragraphs + 1):
                    if i + j < len(blocks):
                        next_block = blocks[i + j].strip()
                        if next_block:
                            succeeding_paragraphs.append(next_block)
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
            
        # 1. Run conversion on raw input PDF to obtain context paragraphs
        self._raw_result = _converter.convert(self.input_path)
        self.raw_markdown = self._raw_result.document.export_to_markdown()
        
        # 2. Resolve target directories for clean pdf
        clean_parent = os.path.dirname(self.output_path)
        if clean_parent:
            os.makedirs(clean_parent, exist_ok=True)
        
        # 3. Redact the hyperlinked text and save to output_path
        self.clean_pdf(self.input_path, self.output_path)
        
        # 4. Convert the clean PDF
        self._parsed_result = _converter.convert(self.output_path)
        self.parsed_markdown = self._parsed_result.document.export_to_markdown()
        
        self._is_parsed = True

    @capture_logs
    @time_function
    @require_parsed
    def extract_table_content_markdown(self):
        print("Extracting table content to Markdown")
        
        # Extract tables and surrounding paragraphs
        tables = self.get_tables(self.parsed_markdown)
        surrounding_paragraphs = self.get_surrounding_paragraphs(self.raw_markdown, num_context_paragraphs=4)
        
        # Construct formatted strings for each table
        table_strings = []
        for i in range(len(tables)):
            table_str = (
                f"-------------- TABLE {i + 1} EXTRACTION --------------\n"
                f"{surrounding_paragraphs[i][0]}\n\n"
                f"{tables[i]}\n\n"
                f"{surrounding_paragraphs[i][1]}"
            )
            table_strings.append(table_str)
                
        return table_strings, self.parsed_markdown, self.logs

    @capture_logs
    @time_function
    @require_parsed
    def extract_table_content_csv(self):
        print("Extracting table content to CSV")
        
        table_csvs = []
        for table in self._parsed_result.document.tables:
            table_df = table.export_to_dataframe(doc=self._parsed_result.document)
            csv_str = table_df.to_csv()
            table_csvs.append(csv_str)
                
        return table_csvs, self.logs
