import os
import sys
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def create_excel(
    dest_path: str,
    base_no_ext: str,
    metadata: dict,
    tables_data: list[dict],
    log_error_fn=None
) -> None:
    """Creates a beautifully formatted Excel document containing both JSON metadata/conditions and CSV table data."""
    def log_error(msg: str):
        if log_error_fn:
            log_error_fn(msg)
        else:
            print(f"REPORT ERROR: {msg}", file=sys.stderr)

    wb = openpyxl.Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    font_family = "Segoe UI"
    
    title_font = Font(name=font_family, size=16, bold=True, color="1F497D")
    title_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    title_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    section_font = Font(name=font_family, size=11, bold=True, color="1F497D")
    section_fill = PatternFill(start_color="B8CCE4", end_color="B8CCE4", fill_type="solid")
    
    label_font = Font(name=font_family, size=10, bold=True, color="333333")
    val_font = Font(name=font_family, size=10, color="000000")
    desc_val_font = Font(name=font_family, size=10, italic=True, color="333333")
    
    table_header_font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
    table_header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    table_header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    thin_border_side = Side(border_style="thin", color="D9D9D9")
    data_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    thick_bottom = Border(bottom=Side(border_style="medium", color="1F497D"))
    
    left_align = Alignment(horizontal="left", vertical="center")
    right_align = Alignment(horizontal="right", vertical="center")
    wrap_left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)

    num_tables = len(tables_data)
    for i in range(num_tables):
        sheet_name = f"Table {i + 1}"
        ws = wb.create_sheet(title=sheet_name)
        ws.views.sheetView[0].showGridLines = True
        
        t_data = tables_data[i]
        table_data = t_data.get("table_data") or {}
        cat_data = t_data.get("cat_data") or {}
        csv_rows = t_data.get("csv_rows")
        csv_error = t_data.get("csv_error")
        
        title_text = metadata.get("title", base_no_ext)
        ws.merge_cells("A1:G2")
        title_cell = ws["A1"]
        title_cell.value = title_text
        title_cell.font = title_font
        title_cell.fill = title_fill
        title_cell.alignment = title_align
        
        for row in range(1, 3):
            for col in range(1, 8):
                cell = ws.cell(row=row, column=col)
                cell.fill = title_fill
                
        ws.cell(row=4, column=1, value="PAPER METADATA & EXPERIMENTAL CONDITIONS").font = section_font
        ws.merge_cells("A4:G4")
        for col in range(1, 8):
            cell = ws.cell(row=4, column=col)
            cell.fill = section_fill
            cell.border = thick_bottom

        def write_metadata_row(r, label, value, is_description=False):
            ws.cell(row=r, column=1, value=label).font = label_font
            ws.cell(row=r, column=1).alignment = left_align
            ws.cell(row=r, column=2, value=value).font = desc_val_font if is_description else val_font
            ws.cell(row=r, column=2).alignment = wrap_left_align
            ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
            for col in range(1, 8):
                ws.cell(row=r, column=col).border = Border(bottom=thin_border_side)
        
        authors_val = ", ".join(metadata.get("authors", [])) if isinstance(metadata.get("authors"), list) else metadata.get("authors", "")
        write_metadata_row(5, "Authors", authors_val)
        write_metadata_row(6, "DOI", metadata.get("doi", ""))
        write_metadata_row(7, "Temperature", table_data.get("temperature", ""))
        write_metadata_row(8, "Pressure", table_data.get("pressure", ""))
        chemicals_val = ", ".join(table_data.get("chemicals", [])) if isinstance(table_data.get("chemicals"), list) else table_data.get("chemicals", "")
        write_metadata_row(9, "Chemicals", chemicals_val)
        
        desc_val = table_data.get("description", "")
        write_metadata_row(10, "Description", desc_val, is_description=True)
        ws.row_dimensions[10].height = 45
        
        other_stats = table_data.get("other_statistics", [])
        stats_str = ""
        if isinstance(other_stats, list):
            stats_str = ", ".join([f"{stat.get('name')}: {stat.get('value')}" for stat in other_stats if isinstance(stat, dict)])
        elif isinstance(other_stats, dict):
            stats_str = ", ".join([f"{k}: {v}" for k, v in other_stats.items()])
        write_metadata_row(11, "Other Stats", stats_str)

        curr_row = 13
        if cat_data:
            ws.cell(row=curr_row, column=1, value="TABLE CATEGORISATION").font = section_font
            ws.merge_cells(start_row=curr_row, start_column=1, end_row=curr_row, end_column=7)
            for col in range(1, 8):
                cell = ws.cell(row=curr_row, column=col)
                cell.fill = section_fill
                cell.border = thick_bottom
            
            curr_row += 1
            def format_bool(val):
                if val is True:
                    return "Yes"
                if val is False:
                    return "No"
                return ""
            write_metadata_row(curr_row, "Contains Scientific Data", format_bool(cat_data.get("contains_scientific_data")))
            curr_row += 1
            write_metadata_row(curr_row, "Contains Diffusion Coefficients", format_bool(cat_data.get("contains_diffusion_coeff")))
            curr_row += 1
            write_metadata_row(curr_row, "Contains Polymer Diffusion Coefficients", format_bool(cat_data.get("contains_polymer_diffusion_coeff")))
            
            curr_row += 2 # gap + dynamic next section start

        start_row = curr_row
        ws.cell(row=start_row, column=1, value="EXTRACTED TABLE DATA").font = section_font
        ws.merge_cells(start_row=start_row, start_column=1, end_row=start_row, end_column=7)
        for col in range(1, 8):
            cell = ws.cell(row=start_row, column=col)
            cell.fill = section_fill
            cell.border = thick_bottom
            
        csv_start_row = start_row + 1
        
        if csv_rows is not None:
            active_row_idx = 0
            for csv_row in csv_rows:
                # Skip empty rows (blank line or list containing only whitespace strings)
                if not csv_row or all(val.strip() == '' for val in csv_row):
                    continue
                    
                curr_row_idx = csv_start_row + active_row_idx
                is_header = (active_row_idx == 0)
                
                for c_idx, val in enumerate(csv_row):
                    cell = ws.cell(row=curr_row_idx, column=c_idx + 1)
                    
                    parsed_val = val
                    try:
                        if "." in val:
                            parsed_val = float(val)
                        else:
                            parsed_val = int(val)
                    except ValueError:
                        pass
                        
                    cell.value = parsed_val
                    cell.border = data_border
                    
                    if is_header:
                        cell.font = table_header_font
                        cell.fill = table_header_fill
                        cell.alignment = table_header_align
                    else:
                        cell.font = val_font
                        if isinstance(parsed_val, (int, float)):
                            cell.alignment = right_align
                        else:
                            cell.alignment = left_align
                    active_row_idx += 1
        elif csv_error is not None:
            ws.cell(row=csv_start_row, column=1, value=f"Error loading CSV data: {csv_error}").font = val_font
        else:
            ws.cell(row=csv_start_row, column=1, value="CSV data file not found.").font = val_font

        excluded_rows = {1, 2, 4, 10, start_row}
        if cat_data:
            excluded_rows.add(13)

        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                if cell.row in excluded_rows:
                    continue
                if cell.value:
                    max_len = max(max_len, len(str(cell.value)))
            ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 40)

    try:
        wb.save(dest_path)
    except Exception as e:
        log_error(f"Error saving Excel document {dest_path}: {e}")


