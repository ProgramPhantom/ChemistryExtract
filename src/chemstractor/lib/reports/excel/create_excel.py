import openpyxl
from chemstractor.lib.reports.helpers import ERROR_SEVERITY_MAP, is_entry_failed
from chemstractor.lib.reports.excel.summary_sheet import build_summary_sheet
from chemstractor.lib.reports.excel.papers_sheet import build_papers_sheet
from chemstractor.lib.reports.excel.polymers_sheet import build_polymers_sheet
from chemstractor.lib.reports.excel.flory_sheet import build_flory_sheet
from chemstractor.lib.reports.excel.mark_houwink_sheet import build_mark_houwink_sheet
from chemstractor.lib.reports.excel.failures_sheet import build_failures_sheet

def create_combined_excel(dest_path: str, combined_data: dict) -> None:
    """Generates a nicely formatted combined Excel report containing Summary, Papers, Polymers, Flory, Mark-Houwink, and Failures sheets."""
    wb = openpyxl.Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    font_family = "Segoe UI"
    
    flory_entries = combined_data.get("flory_entries", [])
    mh_entries = combined_data.get("mark_houwink_entries", [])
    
    # Pre-calculate failure stats for Summary sheet
    failure_reasons_count = {}
    total_mh_failed = 0
    for entry in mh_entries:
        ff = entry.get("failed_fields")
        if isinstance(ff, dict):
            if any(ff.values()):
                total_mh_failed += 1
                for f_key, is_failed in ff.items():
                    if is_failed:
                        lbl = ERROR_SEVERITY_MAP.get(f_key, {}).get("label", f_key)
                        failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif is_entry_failed(entry):
            total_mh_failed += 1

    total_flory_failed = 0
    for entry in flory_entries:
        ff = entry.get("failed_fields")
        if isinstance(ff, dict):
            if any(ff.values()):
                total_flory_failed += 1
                for f_key, is_failed in ff.items():
                    if is_failed:
                        lbl = ERROR_SEVERITY_MAP.get(f_key, {}).get("label", f_key)
                        failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif is_entry_failed(entry):
            total_flory_failed += 1

    total_collected = len(flory_entries) + len(mh_entries)
    total_failures_all = total_flory_failed + total_mh_failed

    # 1. Summary Sheet
    build_summary_sheet(
        wb, combined_data, failure_reasons_count, total_collected, total_failures_all, font_family=font_family
    )

    # 2. Papers Sheet
    papers_summary = combined_data.get("papers_summary", [])
    build_papers_sheet(wb, papers_summary, font_family=font_family)

    # 3. Polymers Sheet
    build_polymers_sheet(wb, flory_entries, font_family=font_family)

    # 4. Flory Sheet
    build_flory_sheet(wb, flory_entries, font_family=font_family)

    # 5. Mark-Houwink Sheet
    build_mark_houwink_sheet(wb, mh_entries, font_family=font_family)

    # 6. Failures Sheet
    build_failures_sheet(wb, flory_entries, mh_entries, font_family=font_family)

    # Freeze top row for all worksheets
    for ws in wb.worksheets:
        ws.freeze_panes = "A2"

    wb.save(dest_path)
