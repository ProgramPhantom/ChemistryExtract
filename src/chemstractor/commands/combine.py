import os
import sys
import json
import time
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich.live import Live

from chemstractor.lib.processor import PDFProcessor
from chemstractor.AI import AI, pricing_matrix
from chemstractor.lib.combiner import gather_and_homogenise

def create_combined_excel(dest_path: str, combined_data: dict) -> None:
    """Generates a nicely formatted combined Excel report containing sheets for Mark-Houwink, Flory, and Failures."""
    wb = openpyxl.Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    font_family = "Segoe UI"
    
    # Styles
    table_header_font = Font(name=font_family, size=10, bold=True, color="FFFFFF")
    table_header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    table_header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    val_font = Font(name=font_family, size=10, color="000000")
    thin_border_side = Side(border_style="thin", color="D9D9D9")
    data_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    
    left_align = Alignment(horizontal="left", vertical="center")
    right_align = Alignment(horizontal="right", vertical="center")
    
    # 1. Mark-Houwink Sheet
    ws_mh = wb.create_sheet(title="Mark-Houwink")
    ws_mh.views.sheetView[0].showGridLines = True
    
    headers_mh = [
        "Source Paper", "Table", "Polymer (Original)", "Polymer (Clean)", 
        "Solvent (Original)", "Solvent (Clean)", "Temperature (K)", 
        "K Value (mL/g)", "K Transformation", "a Value", "a Transformation"
    ]
    
    for col_idx, h in enumerate(headers_mh):
        cell = ws_mh.cell(row=1, column=col_idx + 1, value=h)
        cell.font = table_header_font
        cell.fill = table_header_fill
        cell.alignment = table_header_align
        cell.border = data_border
        
    mh_entries = combined_data.get("mark_houwink_entries", [])
    for row_idx, entry in enumerate(mh_entries):
        r = row_idx + 2
        ws_mh.cell(row=r, column=1, value=entry.get("source_paper", "")).font = val_font
        ws_mh.cell(row=r, column=2, value=entry.get("table_name", "")).font = val_font
        ws_mh.cell(row=r, column=3, value=entry.get("polymer_name_original", "")).font = val_font
        ws_mh.cell(row=r, column=4, value=entry.get("polymer_name", "")).font = val_font
        ws_mh.cell(row=r, column=5, value=entry.get("solvent_original", "")).font = val_font
        ws_mh.cell(row=r, column=6, value=entry.get("solvent", "")).font = val_font
        
        # Numeric values check
        temp = entry.get("temperature_k")
        ws_mh.cell(row=r, column=7, value=float(temp) if temp is not None else None).font = val_font
        
        k_val = entry.get("K_value")
        ws_mh.cell(row=r, column=8, value=float(k_val) if k_val is not None else None).font = val_font
        
        ws_mh.cell(row=r, column=9, value=entry.get("K_transformation", "")).font = val_font
        
        a_val = entry.get("a_value")
        ws_mh.cell(row=r, column=10, value=float(a_val) if a_val is not None else None).font = val_font
        
        ws_mh.cell(row=r, column=11, value=entry.get("a_transformation", "")).font = val_font
        
        for c in [1, 2, 3, 4, 5, 6, 9, 11]:
            ws_mh.cell(row=r, column=c).alignment = left_align
            ws_mh.cell(row=r, column=c).border = data_border
        for c in [7, 8, 10]:
            ws_mh.cell(row=r, column=c).alignment = right_align
            ws_mh.cell(row=r, column=c).border = data_border
            
    # Auto-adjust column width for mh
    for col in ws_mh.columns:
        vals = [str(cell.value or '') for cell in col]
        max_len = max(len(v) for v in vals) if vals else 10
        col_letter = get_column_letter(col[0].column)
        ws_mh.column_dimensions[col_letter].width = max(max_len + 3, 12)
        
    # 2. Flory Sheet
    ws_flory = wb.create_sheet(title="Flory")
    ws_flory.views.sheetView[0].showGridLines = True
    
    headers_flory = [
        "Source Paper", "Table", "Polymer (Original)", "Polymer (Clean)", 
        "Solvent (Original)", "Solvent (Clean)", "Temperature (K)", 
        "c Value (log Constant)", "c Transformation", "v Value (Scaling Exponent)", "v Transformation"
    ]
    
    for col_idx, h in enumerate(headers_flory):
        cell = ws_flory.cell(row=1, column=col_idx + 1, value=h)
        cell.font = table_header_font
        cell.fill = table_header_fill
        cell.alignment = table_header_align
        cell.border = data_border
        
    flory_entries = combined_data.get("flory_entries", [])
    for row_idx, entry in enumerate(flory_entries):
        r = row_idx + 2
        ws_flory.cell(row=r, column=1, value=entry.get("source_paper", "")).font = val_font
        ws_flory.cell(row=r, column=2, value=entry.get("table_name", "")).font = val_font
        ws_flory.cell(row=r, column=3, value=entry.get("polymer_name_original", "")).font = val_font
        ws_flory.cell(row=r, column=4, value=entry.get("polymer_name", "")).font = val_font
        ws_flory.cell(row=r, column=5, value=entry.get("solvent_original", "")).font = val_font
        ws_flory.cell(row=r, column=6, value=entry.get("solvent", "")).font = val_font
        
        temp = entry.get("temperature_k")
        ws_flory.cell(row=r, column=7, value=float(temp) if temp is not None else None).font = val_font
        
        c_val = entry.get("c_value")
        ws_flory.cell(row=r, column=8, value=float(c_val) if c_val is not None else None).font = val_font
        
        ws_flory.cell(row=r, column=9, value=entry.get("c_transformation", "")).font = val_font
        
        v_val = entry.get("v_value")
        ws_flory.cell(row=r, column=10, value=float(v_val) if v_val is not None else None).font = val_font
        
        ws_flory.cell(row=r, column=11, value=entry.get("v_transformation", "")).font = val_font
        
        for c in [1, 2, 3, 4, 5, 6, 9, 11]:
            ws_flory.cell(row=r, column=c).alignment = left_align
            ws_flory.cell(row=r, column=c).border = data_border
        for c in [7, 8, 10]:
            ws_flory.cell(row=r, column=c).alignment = right_align
            ws_flory.cell(row=r, column=c).border = data_border
            
    # Auto-adjust column width for flory
    for col in ws_flory.columns:
        vals = [str(cell.value or '') for cell in col]
        max_len = max(len(v) for v in vals) if vals else 10
        col_letter = get_column_letter(col[0].column)
        ws_flory.column_dimensions[col_letter].width = max(max_len + 3, 12)

    # 3. Failures Sheet
    ws_fail = wb.create_sheet(title="Failures")
    ws_fail.views.sheetView[0].showGridLines = True
    
    headers_fail = ["Source Paper", "Table", "Field Name", "Raw Value", "Failure Reason"]
    for col_idx, h in enumerate(headers_fail):
        cell = ws_fail.cell(row=1, column=col_idx + 1, value=h)
        cell.font = table_header_font
        cell.fill = table_header_fill
        cell.alignment = table_header_align
        cell.border = data_border
        
    failures = combined_data.get("failures", [])
    for row_idx, entry in enumerate(failures):
        r = row_idx + 2
        ws_fail.cell(row=r, column=1, value=entry.get("source_paper", "")).font = val_font
        ws_fail.cell(row=r, column=2, value=entry.get("table", "")).font = val_font
        ws_fail.cell(row=r, column=3, value=entry.get("field", "")).font = val_font
        ws_fail.cell(row=r, column=4, value=entry.get("value", "")).font = val_font
        ws_fail.cell(row=r, column=5, value=entry.get("reason", "")).font = val_font
        
        for c in range(1, 6):
            ws_fail.cell(row=r, column=c).alignment = left_align
            ws_fail.cell(row=r, column=c).border = data_border
            
    # Auto-adjust column width for fail
    for col in ws_fail.columns:
        vals = [str(cell.value or '') for cell in col]
        max_len = max(len(v) for v in vals) if vals else 10
        col_letter = get_column_letter(col[0].column)
        ws_fail.column_dimensions[col_letter].width = max(max_len + 3, 12)

    wb.save(dest_path)

def combine_command(input_dir: str, output_path: str = None, cache_path: str = None) -> None:
    """Executes the combine & homogenisation process across all process output folders in input_dir."""
    console = Console(file=sys.__stdout__)
    
    if not os.path.exists(input_dir):
        console.print(f"[bold red]Error: Input directory '{input_dir}' does not exist.[/bold red]")
        sys.exit(1)
        
    if not os.path.isdir(input_dir):
        console.print(f"[bold red]Error: '{input_dir}' is not a directory.[/bold red]")
        sys.exit(1)
        
    # Default cache path to input_dir/chemical_cache.json if not specified
    if cache_path is None:
        cache_path = os.path.join(input_dir, "chemical_cache.json")
        
    # Default output_path to input_dir/combined_data if not specified
    if output_path is None:
        output_prefix = os.path.join(input_dir, "combined_data")
    else:
        # Check if it has extension or represents a folder
        if output_path.endswith(".json") or output_path.endswith(".xlsx"):
            output_prefix = os.path.splitext(output_path)[0]
        else:
            output_prefix = os.path.join(output_path, "combined_data")
            
    # Resolve exact file paths
    json_out = f"{output_prefix}.json"
    xlsx_out = f"{output_prefix}.xlsx"
    
    # 1. Grab all subdirectories in input_dir
    subfolders = [
        os.path.join(input_dir, d) for d in os.listdir(input_dir)
        if os.path.isdir(os.path.join(input_dir, d))
    ]
    
    # 2. Filter directories that look like process outputs
    valid_subfolders = []
    for sf in subfolders:
        extract_dir = os.path.join(sf, "extract")
        interp_dir = os.path.join(sf, "interpretation")
        if os.path.isdir(extract_dir) or os.path.isdir(interp_dir):
            valid_subfolders.append(sf)
            
    if not valid_subfolders:
        console.print("[bold red]Error: No subfolders containing extracted or interpreted data found in the input directory.[/bold red]")
        sys.exit(1)
        
    console.print(Rule(title=f"[bold magenta]COMBINING & HOMOGENISING DATA ({len(valid_subfolders)} PAPERS)[/bold magenta]", style="magenta"))
    console.print(f"Inputs dir: [cyan]{input_dir}[/cyan]")
    console.print(f"Cache file: [cyan]{cache_path}[/cyan]")
    console.print()
    
    # 3. Load PDFProcessor instances
    processors = []
    with console.status("[bold green]Loading process outputs into PDFProcessors...", spinner="dots"):
        for sf in sorted(valid_subfolders):
            try:
                proc = PDFProcessor()
                proc.load_output(sf)
                # Check if there is actual interpretation data
                has_interp = any(item is not None for item in proc.interpretation_data_list)
                if has_interp:
                    processors.append(proc)
            except Exception as e:
                console.print(f"[yellow]⚠[/yellow] Warning: Failed to load processor output from '{sf}': {e}")
                
    if not processors:
        console.print("[bold yellow]No papers with valid interpretation data were found. Nothing to combine.[/bold yellow]")
        return
        
    console.print(f"Loaded [green]{len(processors)}[/green] papers containing interpreted table data.")
    
    # 4. Run homogenisation data pipeline
    start_time = time.time()
    ai_instance = AI.get_instance()
    selected_model = ai_instance.selected_model
    
    with console.status(f"[bold cyan]Running chemical name homogenisation using {selected_model}...[/bold cyan]", spinner="dots"):
        results = gather_and_homogenise(processors, cache_path, ai_instance)
        
    elapsed = time.time() - start_time
    
    # 5. Write outputs
    try:
        # Create output folders if they do not exist
        out_dir = os.path.dirname(json_out)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
            
        with open(json_out, 'w', encoding='utf-8') as jf:
            json.dump(results, jf, indent=2, ensure_ascii=False)
            
        create_combined_excel(xlsx_out, results)
        
    except Exception as e:
        console.print(f"[bold red]Error saving outputs: {e}[/bold red]")
        sys.exit(1)
        
    # 6. Report results and statistics
    console.print()
    console.print(f"[bold green]✓[/bold green] Combining process completed in [yellow]{elapsed:.2f}s[/yellow].")
    console.print(f"JSON data saved to: [cyan]{json_out}[/cyan]")
    console.print(f"Excel report saved to: [cyan]{xlsx_out}[/cyan]")
    console.print()
    
    # Statistics Table
    stats = results.get("stats", {})
    t = Table(title="Homogenisation Statistics", header_style="bold magenta")
    t.add_column("Metric", style="cyan")
    t.add_column("Count", style="green")
    
    t.add_row("Total Chemical Fields Checked", str(stats.get("total_processed", 0)))
    t.add_row("Cache Hits (Fuzzy + Exact)", str(stats.get("cache_hits", 0)))
    t.add_row("AI Match Hits (Enum Selection)", str(stats.get("ai_match_hits", 0)))
    t.add_row("AI Generated Names (New)", str(stats.get("ai_generated", 0)))
    t.add_row("Failed / Non-Chemical Fields (N/A)", str(stats.get("failed", 0)))
    console.print(t)
    
    failures = results.get("failures", [])
    if failures:
        console.print()
        console.print(f"[bold yellow]Recorded Failures ({len(failures)}):[/bold yellow]")
        for f in failures[:15]:
            console.print(f" - [dim]{f['source_paper']}/{f['table']}[/dim]: Field [cyan]{f['field']}[/cyan] with value '[red]{f['value']}[/red]' -> [yellow]{f['reason']}[/yellow]")
        if len(failures) > 15:
            console.print(f" ... and {len(failures) - 15} more failures. See the failures sheet in Excel/JSON.")
            
    # Calculate token counts and pricing
    # (Since AI prompt increments these totals, we can report model total costs)
    total_in = ai_instance.total_prompt_tokens
    total_out = ai_instance.total_candidate_tokens
    if total_in > 0 or total_out > 0:
        cost_str = ""
        if selected_model in pricing_matrix:
            pricing = pricing_matrix[selected_model]
            cost = (total_in * pricing["input_per_m"] + total_out * pricing["output_per_m"]) / 1_000_000
            cost_str = f" ($ {cost:.6f})"
        console.print()
        console.print(f"AI Usage during run: [magenta]{selected_model}[/magenta] - [dim]{total_in} input tokens, {total_out} output tokens{cost_str}[/dim]")
