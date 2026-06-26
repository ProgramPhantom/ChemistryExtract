import time
import sys
from rich.console import Console

console = Console(file=sys.__stdout__)
start_time = time.time()

with console.status("[bold yellow]Loading Docling models and dependencies...[/bold yellow]"):
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import DocumentStream
    from io import BytesIO
    import pandas as pd
    import fitz  # PyMuPDF
    import os
    import glob
    from datetime import datetime
    import logging
    from contextlib import redirect_stdout, redirect_stderr, contextmanager
    import io
    from functools import wraps

    _converter = DocumentConverter()

elapsed = time.time() - start_time
console.print(f"[bold green]✓[/bold green] Docling loaded in [yellow]{elapsed:.2f}s[/yellow]")

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


class TableExtractor:
    @property
    def logs(self) -> str:
        return self.log_stream.getvalue()

    def __init__(self, input_path: str):
        self.log_stream = io.StringIO()
        self._is_capturing = False

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
        
        # Parse PDF immediately upon instantiation
        self.parse_pdf()
        # Extract tables and CSV data immediately
        self.extract_results()

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

    def clean_pdf(self):
        self.redact_hyperlinked_text()

    def redact_hyperlinked_text(self):
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
        print("All hyperlinked elements redacted in-memory.")

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
        
        # 2. Redact the hyperlinked text in-memory
        self.clean_pdf()
        
        # 3. Convert the clean PDF from in-memory bytes
        filename = os.path.basename(self.input_path)
        stream = DocumentStream(name=f"clean_{filename}", stream=BytesIO(self.clean_pdf_bytes))
        self._parsed_result = _converter.convert(stream)
        self.parsed_markdown = self._parsed_result.document.export_to_markdown()
        
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
            csv_str = table_df.to_csv()
            self.tables_csv.append(csv_str)