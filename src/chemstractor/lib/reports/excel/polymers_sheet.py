import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import LineChart, Reference, Series
from chemstractor.lib.reports.helpers import is_entry_failed

def try_parse_float(val) -> float | None:
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        try:
            return float(val.strip())
        except ValueError:
            return None
    return None

def is_flory_entry_valid(entry: dict) -> bool:
    """Checks if a Flory entry is valid for inclusion in the Polymers sheet."""
    c_val = try_parse_float(entry.get("c_value"))
    v_val = try_parse_float(entry.get("v_value"))
    p_name = entry.get("polymer_name")
    s_name = entry.get("solvent_name", entry.get("solvent"))

    if c_val is None or v_val is None:
        return False
    if p_name in (None, "", "N/A", "Invalid chemical") or s_name in (None, "", "N/A", "Invalid chemical"):
        return False

    ff = entry.get("failed_fields")
    if isinstance(ff, dict):
        # Temperature missing is a warning and should be included
        critical_failures = [k for k, v in ff.items() if v and k != "temperature_missing"]
        if critical_failures:
            return False
    elif isinstance(ff, str) and ff != "None":
        return False

    return True

def build_polymers_sheet(wb, flory_entries: list, font_family: str = "Segoe UI") -> None:
    """Builds the interactive Polymers worksheet in the Excel workbook."""
    ws_poly = wb.create_sheet(title="Polymers")
    ws_poly.views.sheetView[0].showGridLines = True

    # Styling definitions
    title_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")
    title_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    
    table_header_font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
    table_header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    table_header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    label_font = Font(name=font_family, size=10, bold=True, color="1F497D")
    val_font = Font(name=font_family, size=10, color="000000")
    
    thin_border_side = Side(border_style="thin", color="D9D9D9")
    data_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    
    left_align = Alignment(horizontal="left", vertical="center")
    right_align = Alignment(horizontal="right", vertical="center")
    center_align = Alignment(horizontal="center", vertical="center")

    # Filter out failed entries
    valid_flory_poly = [entry for entry in flory_entries if is_flory_entry_valid(entry)]

    # Sort Flory entries polymer-centric
    sorted_flory_poly = sorted(
        valid_flory_poly, 
        key=lambda x: (
            (x.get("polymer_name") or "").lower(),
            (x.get("solvent_name") or x.get("solvent") or "").lower()
        )
    )

    # Gather unique polymers and solvents for dropdown lists
    unique_polymers = ["All"] + sorted(list({e.get("polymer_name") for e in sorted_flory_poly if e.get("polymer_name")}))
    unique_solvents = ["All"] + sorted(list({e.get("solvent_name", e.get("solvent")) for e in sorted_flory_poly if e.get("solvent_name", e.get("solvent"))}))

    # Populate Data Validation helper columns in Columns L (Polymer list) and M (Solvent list)
    for idx, p in enumerate(unique_polymers, start=2):
        ws_poly.cell(row=idx, column=12, value=p).font = val_font
    for idx, s in enumerate(unique_solvents, start=2):
        ws_poly.cell(row=idx, column=13, value=s).font = val_font

    # Hide helper columns L and M
    ws_poly.column_dimensions["L"].hidden = True
    ws_poly.column_dimensions["M"].hidden = True

    # 1. Interactive Control Panel (Rows 2 - 5, Columns B & C)
    ws_poly.merge_cells("B2:C2")
    ctrl_title_cell = ws_poly.cell(row=2, column=2, value="Interactive Curve Explorer")
    ctrl_title_cell.font = title_font
    ctrl_title_cell.fill = title_fill
    ctrl_title_cell.alignment = center_align
    ctrl_title_cell.border = data_border
    ws_poly.cell(row=2, column=3).border = data_border

    # Select Polymer row
    lbl_poly = ws_poly.cell(row=3, column=2, value="Select Polymer:")
    lbl_poly.font = label_font
    lbl_poly.alignment = Alignment(horizontal="right", vertical="center")
    lbl_poly.border = data_border

    val_poly = ws_poly.cell(row=3, column=3, value="All")
    val_poly.font = val_font
    val_poly.alignment = left_align
    val_poly.border = data_border

    # Add Polymer Data Validation
    dv_poly = DataValidation(
        type="list", 
        formula1=f"=Polymers!$L$2:$L${len(unique_polymers)+1}", 
        allow_blank=True
    )
    ws_poly.add_data_validation(dv_poly)
    dv_poly.add(val_poly)

    # Select Solvent row
    lbl_solv = ws_poly.cell(row=4, column=2, value="Select Solvent:")
    lbl_solv.font = label_font
    lbl_solv.alignment = Alignment(horizontal="right", vertical="center")
    lbl_solv.border = data_border

    val_solv = ws_poly.cell(row=4, column=3, value="All")
    val_solv.font = val_font
    val_solv.alignment = left_align
    val_solv.border = data_border

    # Add Solvent Data Validation
    dv_solv = DataValidation(
        type="list", 
        formula1=f"=Polymers!$M$2:$M${len(unique_solvents)+1}", 
        allow_blank=True
    )
    ws_poly.add_data_validation(dv_solv)
    dv_solv.add(val_solv)

    # Summary row: Active Curves count
    start_data_row = 20
    end_data_row = start_data_row + len(sorted_flory_poly) - 1 if sorted_flory_poly else start_data_row

    lbl_count = ws_poly.cell(row=5, column=2, value="Active Curves:")
    lbl_count.font = label_font
    lbl_count.alignment = Alignment(horizontal="right", vertical="center")
    lbl_count.border = data_border

    val_count = ws_poly.cell(row=5, column=3, value=f'=COUNTIF(F{start_data_row}:F{max(end_data_row, start_data_row)}, "<>#N/A")')
    val_count.font = label_font
    val_count.alignment = left_align
    val_count.border = data_border

    # 2. Main Data Table Header (Row 19)
    headers_poly = [
        "Polymer (Clean)", "Solvent (Clean)", "Temperature (K)", 
        "c Value (log Constant)", "v Value (Scaling Exponent)", "3", "6"
    ]
    header_row = 19
    for col_idx, h in enumerate(headers_poly, start=1):
        cell = ws_poly.cell(row=header_row, column=col_idx, value=h if not h.isdigit() else int(h))
        cell.font = table_header_font
        cell.fill = table_header_fill
        cell.alignment = table_header_align
        cell.border = data_border

    # Fill Main Data Table rows
    y_vals = []
    for row_offset, entry in enumerate(sorted_flory_poly):
        r = start_data_row + row_offset
        ws_poly.cell(row=r, column=1, value=entry.get("polymer_name", "")).font = val_font
        ws_poly.cell(row=r, column=2, value=entry.get("solvent_name", entry.get("solvent", ""))).font = val_font

        temp = entry.get("temperature_k")
        ws_poly.cell(row=r, column=3, value=float(temp) if isinstance(temp, (int, float)) else temp).font = val_font

        c_val = entry.get("c_value")
        ws_poly.cell(row=r, column=4, value=float(c_val) if isinstance(c_val, (int, float)) else c_val).font = val_font

        v_val = entry.get("v_value")
        ws_poly.cell(row=r, column=5, value=float(v_val) if isinstance(v_val, (int, float)) else v_val).font = val_font

        # Dynamic formula: Evaluate to numeric log value if matching Polymer and Solvent selection, else NA()
        formula_filter = f"AND(OR($C$3=\"All\", $C$3=\"\", A{r}=$C$3), OR($C$4=\"All\", $C$4=\"\", B{r}=$C$4))"
        ws_poly.cell(row=r, column=6, value=f"=IF({formula_filter}, D{r}-E{r}*3, NA())").font = val_font
        ws_poly.cell(row=r, column=7, value=f"=IF({formula_filter}, D{r}-E{r}*6, NA())").font = val_font

        if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)):
            y_vals.append(c_val - v_val * 3)
            y_vals.append(c_val - v_val * 6)

        for c in [1, 2]:
            ws_poly.cell(row=r, column=c).alignment = left_align
            ws_poly.cell(row=r, column=c).border = data_border
        for c in range(3, 8):
            ws_poly.cell(row=r, column=c).alignment = right_align
            ws_poly.cell(row=r, column=c).border = data_border

    # 3. Interactive Flory Line Chart
    if sorted_flory_poly:
        try:
            chart_flory = LineChart()
            chart_flory.title = "Flory Calibration Curves (Interactive log-log Plot)"
            chart_flory.style = 13
            chart_flory.x_axis.title = "log(M / g mol⁻¹)"
            chart_flory.y_axis.title = "log(D / m² s⁻¹)"
            chart_flory.x_axis.delete = False
            chart_flory.y_axis.delete = False
            chart_flory.x_axis.tickLblPos = "low"
            chart_flory.y_axis.tickLblPos = "nextTo"

            if y_vals:
                min_y = min(y_vals)
                max_y = max(y_vals)
                chart_flory.y_axis.scaling.min = float(f"{min_y - 0.5:.2f}")
                chart_flory.y_axis.scaling.max = float(f"{max_y + 0.5:.2f}")

            chart_flory.width = 18
            chart_flory.height = 13

            for row_offset, entry in enumerate(sorted_flory_poly):
                r = start_data_row + row_offset
                series_ref = Reference(ws_poly, min_col=6, max_col=7, min_row=r, max_row=r)
                solv_str = entry.get('solvent_name', entry.get('solvent'))
                series = Series(series_ref, title=f"{entry.get('polymer_name')} in {solv_str}")
                chart_flory.append(series)

            cats_ref = Reference(ws_poly, min_col=6, max_col=7, min_row=header_row, max_row=header_row)
            chart_flory.set_categories(cats_ref)

            colors = ["1F497D", "C0504D", "9BBB59", "8064A2", "F79646", "4BACC6", "E26B0A", "7030A0", "00B0F0"]
            for s_idx, series in enumerate(chart_flory.series):
                color = colors[s_idx % len(colors)]
                series.graphicalProperties.line = openpyxl.drawing.line.LineProperties(solidFill=color)

            ws_poly.add_chart(chart_flory, "E2")
        except Exception:
            pass

    # Auto-adjust column widths (excluding hidden helper columns)
    for col in ws_poly.columns:
        col_letter = get_column_letter(col[0].column)
        if col_letter in ("L", "M"):
            continue
        vals = [str(cell.value or '') for cell in col if cell.row >= header_row or cell.column in (1, 2, 3)]
        max_len = max(len(v) for v in vals) if vals else 10
        ws_poly.column_dimensions[col_letter].width = max(max_len + 3, 14)
