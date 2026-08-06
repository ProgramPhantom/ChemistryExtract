from __future__ import annotations
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import LineChart, Reference, Series
from openpyxl.chart.series import SeriesLabel
from openpyxl.chart.data_source import StrRef
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
    ws_poly = wb.create_sheet(title="Results")
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

    # Row positioning definitions (Data table at top: header at row 1, data starts at row 2)
    header_row = 1
    start_data_row = 2
    end_data_row = start_data_row + len(sorted_flory_poly) - 1 if sorted_flory_poly else start_data_row

    data_range_a = f"$A$2:$A${max(end_data_row, 2)}"
    data_range_b = f"$B$2:$B${max(end_data_row, 2)}"

    # Data explorer dropdown selections are in M2 (Polymer) and M3 (Solvent)
    sel_poly_clean = "IF(OR(LEFT($M$2, 3)=\"All\", $M$2=\"\"), \"*\", LEFT($M$2, IF(ISNUMBER(SEARCH(\" (\", $M$2)), SEARCH(\" (\", $M$2)-1, LEN($M$2))))"
    sel_solv_clean = "IF(OR(LEFT($M$3, 3)=\"All\", $M$3=\"\"), \"*\", LEFT($M$3, IF(ISNUMBER(SEARCH(\" (\", $M$3)), SEARCH(\" (\", $M$3)-1, LEN($M$3))))"

    # Helper Column P: Raw Unique Polymers
    for idx, p in enumerate(unique_polymers, start=2):
        ws_poly.cell(row=idx, column=16, value=p).font = val_font

    # Helper Column Q: Raw Unique Solvents
    for idx, s in enumerate(unique_solvents, start=2):
        ws_poly.cell(row=idx, column=17, value=s).font = val_font

    # Helper Column R: Dynamic Solvent List with Counts (Evaluating selected Polymer M2)
    ws_poly.cell(row=2, column=18, value=f'=Q2 & " (" & COUNTIFS({data_range_a}, {sel_poly_clean}) & ")"').font = val_font
    for idx, s in enumerate(unique_solvents[1:], start=3):
        ws_poly.cell(row=idx, column=18, value=f'=Q{idx} & " (" & COUNTIFS({data_range_a}, {sel_poly_clean}, {data_range_b}, Q{idx}) & ")"').font = val_font

    # Helper Column S: Dynamic Polymer List with Counts (Evaluating selected Solvent M3)
    ws_poly.cell(row=2, column=19, value=f'=P2 & " (" & COUNTIFS({data_range_b}, {sel_solv_clean}) & ")"').font = val_font
    for idx, p in enumerate(unique_polymers[1:], start=3):
        ws_poly.cell(row=idx, column=19, value=f'=P{idx} & " (" & COUNTIFS({data_range_a}, P{idx}, {data_range_b}, {sel_solv_clean}) & ")"').font = val_font

    # Hide helper columns J, P, Q, R, S
    for c_letter in ("J", "P", "Q", "R", "S"):
        ws_poly.column_dimensions[c_letter].hidden = True

    # 1. Main Data Table Header (Row 1)
    headers_poly = [
        "Polymer (Clean)", "Solvent (Clean)", "Temperature (K)", 
        "c Value (log Constant)", "v Value (Scaling Exponent)", "3", "6",
        "Source Paper", "Table"
    ]
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
        formula_filter = (
            f"AND("
            f"OR(LEFT($M$2, 3)=\"All\", $M$2=\"\", $M$2=A{r}, AND(LEFT($M$2, LEN(A{r}))=A{r}, MID($M$2, LEN(A{r})+1, 2)=\" (\")), "
            f"OR(LEFT($M$3, 3)=\"All\", $M$3=\"\", $M$3=B{r}, AND(LEFT($M$3, LEN(B{r}))=B{r}, MID($M$3, LEN(B{r})+1, 2)=\" (\"))"
            f")"
        )
        ws_poly.cell(row=r, column=6, value=f"=IF({formula_filter}, D{r}-E{r}*3, NA())").font = val_font
        ws_poly.cell(row=r, column=7, value=f"=IF({formula_filter}, D{r}-E{r}*6, NA())").font = val_font

        ws_poly.cell(row=r, column=8, value=entry.get("source_paper", "")).font = val_font
        ws_poly.cell(row=r, column=9, value=entry.get("table_name", "")).font = val_font

        # Dynamic Series Title in Column J (col 10) for plot legend
        title_formula = (
            f"IF(AND(OR(LEFT($M$2, 3)=\"All\", $M$2=\"\"), OR(LEFT($M$3, 3)=\"All\", $M$3=\"\")), A{r} & \" in \" & B{r}, "
            f"IF(OR(LEFT($M$2, 3)<>\"All\", $M$2<=\"\"), B{r}, A{r}))"
        )
        ws_poly.cell(row=r, column=10, value=f"={title_formula}").font = val_font

        if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)):
            y_vals.append(c_val - v_val * 3)
            y_vals.append(c_val - v_val * 6)

        for c in [1, 2, 8, 9, 10]:
            ws_poly.cell(row=r, column=c).alignment = left_align
            ws_poly.cell(row=r, column=c).border = data_border
        for c in range(3, 8):
            ws_poly.cell(row=r, column=c).alignment = right_align
            ws_poly.cell(row=r, column=c).border = data_border

    # Enable native Excel AutoFilter on the main data table
    ws_poly.auto_filter.ref = f"A{header_row}:I{max(end_data_row, start_data_row)}"

    # 2. Interactive Control Panel (Right hand side: Rows 1 - 3, Columns L & M)
    ws_poly.merge_cells("L1:M1")
    ctrl_title_cell = ws_poly.cell(row=1, column=12, value="Data explorer")
    ctrl_title_cell.font = title_font
    ctrl_title_cell.fill = title_fill
    ctrl_title_cell.alignment = center_align
    ctrl_title_cell.border = data_border
    ws_poly.cell(row=1, column=13).border = data_border

    # Select Polymer row (Row 2, Cols L & M)
    lbl_poly = ws_poly.cell(row=2, column=12, value="Select Polymer:")
    lbl_poly.font = label_font
    lbl_poly.alignment = Alignment(horizontal="right", vertical="center")
    lbl_poly.border = data_border

    val_poly = ws_poly.cell(row=2, column=13, value="All")
    val_poly.font = val_font
    val_poly.alignment = left_align
    val_poly.border = data_border

    # Add Polymer Data Validation (Pointing to Column S)
    dv_poly = DataValidation(
        type="list", 
        formula1=f"=Results!$S$2:$S${len(unique_polymers)+1}", 
        allow_blank=True
    )
    ws_poly.add_data_validation(dv_poly)
    dv_poly.add(val_poly)

    # Select Solvent row (Row 3, Cols L & M)
    lbl_solv = ws_poly.cell(row=3, column=12, value="Select Solvent:")
    lbl_solv.font = label_font
    lbl_solv.alignment = Alignment(horizontal="right", vertical="center")
    lbl_solv.border = data_border

    val_solv = ws_poly.cell(row=3, column=13, value="All")
    val_solv.font = val_font
    val_solv.alignment = left_align
    val_solv.border = data_border

    # Add Solvent Data Validation (Pointing to Column R)
    dv_solv = DataValidation(
        type="list", 
        formula1=f"=Results!$R$2:$R${len(unique_solvents)+1}", 
        allow_blank=True
    )
    ws_poly.add_data_validation(dv_solv)
    dv_solv.add(val_solv)

    # 3. Interactive Flory Line Chart (Placed at L5 on the right hand side)
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
            chart_flory.visible_cells_only = True

            for row_offset, entry in enumerate(sorted_flory_poly):
                r = start_data_row + row_offset
                series_ref = Reference(ws_poly, min_col=6, max_col=7, min_row=r, max_row=r)
                series = Series(series_ref)
                series.title = SeriesLabel(strRef=StrRef(f=f"Results!$J${r}"))
                chart_flory.append(series)

            cats_ref = Reference(ws_poly, min_col=6, max_col=7, min_row=header_row, max_row=header_row)
            chart_flory.set_categories(cats_ref)

            colors = ["1F497D", "C0504D", "9BBB59", "8064A2", "F79646", "4BACC6", "E26B0A", "7030A0", "00B0F0"]
            for s_idx, series in enumerate(chart_flory.series):
                color = colors[s_idx % len(colors)]
                series.graphicalProperties.line = openpyxl.drawing.line.LineProperties(solidFill=color)

            ws_poly.add_chart(chart_flory, "L5")
        except Exception:
            pass

    # Auto-adjust column widths (excluding hidden helper columns)
    for col in ws_poly.columns:
        col_letter = get_column_letter(col[0].column)
        if col_letter in ("J", "P", "Q", "R", "S"):
            continue
        vals = [str(cell.value or '') for cell in col if cell.row >= header_row or cell.column in (1, 2, 12, 13)]
        max_len = max(len(v) for v in vals) if vals else 10
        ws_poly.column_dimensions[col_letter].width = max(max_len + 3, 14)
