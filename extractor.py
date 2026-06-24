from docling.document_converter import DocumentConverter
import fitz  # PyMuPDF
import os
import glob
from datetime import datetime
import logging
from contextlib import redirect_stdout, redirect_stderr
import io


def clean_pdf(input_path, output_path):
    redact_hyperlinked_text(input_path, output_path)


def redact_hyperlinked_text(input_path, output_path):
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


def get_tables(doc_str: str) -> list[str]:
    blocks = doc_str.split('\n\n')
    table_strings = []

    for i, block in enumerate(blocks):
        # A standard Markdown table contains a header separator row like "|---"
        if '|---' in block or '| ---' in block:
            # Add the table itself
            table_strings.append(f"**[Table Data]**\n{block.strip()}")

    # 3. Join the extracted blocks back into a single string
    return table_strings


def get_surrounding_paragraphs(doc_str: str, num_context_paragraphs: int = 1) -> list[tuple[str, str]]:
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


def extract_table_content(input_path, clean_pdf_output=""):
    log_capture = io.StringIO()

    with redirect_stdout(log_capture), redirect_stderr(log_capture):
        root_logger = logging.getLogger()
        temp_handler = logging.StreamHandler(log_capture)
        root_logger.addHandler(temp_handler)
        
        try:
            converter = DocumentConverter()
            
            # 1. Run conversion on raw input PDF to obtain context paragraphs
            raw_result = converter.convert(input_path)
            raw_markdown = raw_result.document.export_to_markdown()
            
            # 2. Extract input directory and base filename
            input_dir = os.path.dirname(input_path)
            filename = os.path.basename(input_path)
            
            # 3. Resolve the clean path dynamically based on clean_pdf_output
            if clean_pdf_output:
                if clean_pdf_output.lower().endswith('.pdf'):
                    clean_path = clean_pdf_output
                else:
                    clean_path = os.path.join(clean_pdf_output, f"clean_{filename}")
            else:
                clean_dir = os.path.join(input_dir, "clean")
                os.makedirs(clean_dir, exist_ok=True)
                clean_path = os.path.join(clean_dir, f"clean_{filename}")
                
            clean_parent = os.path.dirname(clean_path)
            if clean_parent:
                os.makedirs(clean_parent, exist_ok=True)
            
            # 4. Redact the hyperlinked text and save to clean_path
            clean_pdf(input_path, clean_path)
            
            # 5. Convert the clean PDF
            parsed_result = converter.convert(clean_path)
            parsed_markdown = parsed_result.document.export_to_markdown()
            
            # 6. Extract tables and surrounding paragraphs
            tables = get_tables(parsed_markdown)
            surrounding_paragraphs = get_surrounding_paragraphs(raw_markdown, num_context_paragraphs=4)
            
            # 7. Construct formatted strings for each table
            table_strings = []
            for i in range(len(tables)):
                table_str = (
                    f"-------------- TABLE {i + 1} EXTRACTION --------------\n"
                    f"{surrounding_paragraphs[i][0]}\n\n"
                    f"{tables[i]}\n\n"
                    f"{surrounding_paragraphs[i][1]}"
                )
                table_strings.append(table_str)
                
        finally:
            root_logger.removeHandler(temp_handler)
            
    return table_strings, log_capture.getvalue()


