from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

def build_polymers_sheet(wb, flory_entries: list, font_family: str = "Segoe UI") -> None:
    """Builds the Polymers worksheet in the Excel workbook."""
    ws_poly = wb.create_sheet(title="Polymers")
    ws_poly.views.sheetView[0].showGridLines = True

    table_header_font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
    table_header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    table_header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    val_font = Font(name=font_family, size=10, color="000000")
    thin_border_side = Side(border_style="thin", color="D9D9D9")
    data_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    left_align = Alignment(horizontal="left", vertical="center")
    right_align = Alignment(horizontal="right", vertical="center")

    headers_poly = [
        "Polymer (Clean)", "Solvent (Clean)", "Temperature (K)", 
        "c Value (log Constant)", "v Value (Scaling Exponent)", "3", "6"
    ]
    for col_idx, h in enumerate(headers_poly):
        cell = ws_poly.cell(row=1, column=col_idx + 1, value=h)
        cell.font = table_header_font
        cell.fill = table_header_fill
        cell.alignment = table_header_align
        cell.border = data_border

    # Filter out failed entries
    valid_flory_poly = []
    for entry in flory_entries:
        c_val = entry.get("c_value")
        v_val = entry.get("v_value")
        has_failed = entry.get("failed_fields", "None") != "None" or entry.get("polymer_name") == "N/A" or entry.get("solvent") == "N/A"
        if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)) and not has_failed:
            valid_flory_poly.append(entry)

    # Sort Flory entries polymer-centric
    sorted_flory_poly = sorted(
        valid_flory_poly, 
        key=lambda x: (
            (x.get("polymer_name") or "").lower(),
            (x.get("solvent") or "").lower()
        )
    )

    for row_idx, entry in enumerate(sorted_flory_poly):
        r = row_idx + 2
        ws_poly.cell(row=r, column=1, value=entry.get("polymer_name", "")).font = val_font
        ws_poly.cell(row=r, column=2, value=entry.get("solvent", "")).font = val_font

        temp = entry.get("temperature_k")
        ws_poly.cell(row=r, column=3, value=float(temp) if isinstance(temp, (int, float)) else temp).font = val_font

        c_val = entry.get("c_value")
        ws_poly.cell(row=r, column=4, value=float(c_val) if isinstance(c_val, (int, float)) else c_val).font = val_font

        v_val = entry.get("v_value")
        ws_poly.cell(row=r, column=5, value=float(v_val) if isinstance(v_val, (int, float)) else v_val).font = val_font

        ws_poly.cell(row=r, column=6, value=f"=D{r}-E{r}*3").font = val_font
        ws_poly.cell(row=r, column=7, value=f"=D{r}-E{r}*6").font = val_font

        for c in [1, 2]:
            ws_poly.cell(row=r, column=c).alignment = left_align
            ws_poly.cell(row=r, column=c).border = data_border
        for c in range(3, 8):
            ws_poly.cell(row=r, column=c).alignment = right_align
            ws_poly.cell(row=r, column=c).border = data_border

    for col in ws_poly.columns:
        vals = [str(cell.value or '') for cell in col]
        max_len = max(len(v) for v in vals) if vals else 10
        col_letter = get_column_letter(col[0].column)
        ws_poly.column_dimensions[col_letter].width = max(max_len + 3, 12)
