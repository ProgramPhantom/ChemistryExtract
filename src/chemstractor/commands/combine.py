from chemstractor.lib.combiner import save_cache
from chemstractor.lib.combiner import load_cache
import os
import sys
import json
import time
from datetime import datetime
import pandas as pd
import matplotlib
matplotlib.use("Agg")
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TaskProgressColumn, TimeElapsedColumn, MofNCompleteColumn
from rich.tree import Tree
from rich.console import Group

from chemstractor.lib.processor import PDFProcessor
from chemstractor.AI import AI, pricing_matrix
from chemstractor.lib.combiner import load_and_homogenise, sort_and_save

from chemstractor.lib.reports import (
    ERROR_SEVERITY_MAP,
    SEVERITY_PRIORITY,
    is_entry_failed,

)
from chemstractor.lib.reports.excel import create_combined_excel
from chemstractor.lib.reports.diagram import create_plots




def build_flat_databases(results: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Builds flat (unaggregated) pandas DataFrames for Flory and Mark-Houwink entries from results."""
    # 1. Flory flat database
    flory_entries = results.get("flory_entries", [])
    valid_flory = [entry for entry in flory_entries if not is_entry_failed(entry)]
        
    records_flory = []
    for entry in valid_flory:
        records_flory.append({
            "solvent": entry.get("solvent_name", entry.get("solvent")),
            "polymer": entry.get("polymer_name"),
            "c_value": entry.get("c_value"),
            "v_value": entry.get("v_value"),
            "source_paper": entry.get("source_paper"),
            "table_name": entry.get("table_name")
        })
    df_flory = pd.DataFrame(records_flory)
    if df_flory.empty:
        df_flory = pd.DataFrame(columns=["solvent", "polymer", "c_value", "v_value", "source_paper", "table_name"])
        
    # 2. Mark-Houwink flat database
    mh_entries = results.get("mark_houwink_entries", [])
    valid_mh = [entry for entry in mh_entries if not is_entry_failed(entry)]
        
    records_mh = []
    for entry in valid_mh:
        records_mh.append({
            "solvent": entry.get("solvent_name", entry.get("solvent")),
            "polymer": entry.get("polymer_name"),
            "K_value": entry.get("K_value"),
            "a_value": entry.get("a_value"),
            "source_paper": entry.get("source_paper"),
            "table_name": entry.get("table_name")
        })
    df_mh = pd.DataFrame(records_mh)
    if df_mh.empty:
        df_mh = pd.DataFrame(columns=["solvent", "polymer", "K_value", "a_value", "source_paper", "table_name"])

    return df_flory, df_mh


def combine_command(input_dir: str, output_path: str = None, cache_path: str = None, pdf_dir: str = None, process_manifest: dict = None) -> None:
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
        
    dateTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
    # Default output_path to input_dir/combined_data_{dateTime} if not specified
    if output_path is None:
        output_prefix = os.path.join(input_dir, f"combined_data_{dateTime}")
    else:
        # Check if it has extension or represents a folder
        if output_path.endswith(".json") or output_path.endswith(".xlsx"):
            output_prefix = f"{os.path.splitext(output_path)[0]}_{dateTime}"
        else:
            output_prefix = os.path.join(output_path, f"combined_data_{dateTime}")
            
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
                has_interp = (
                    any(item is not None for item in proc.interpretation_flory_data_list) or
                    any(item is not None for item in proc.interpretation_mh_data_list)
                )
                if has_interp:
                    processors.append(proc)
            except Exception as e:
                console.print(f"[yellow]⚠[/yellow] Warning: Failed to load processor output from '{sf}': {e}")
                
    if not processors:
        console.print("[bold yellow]No papers with valid interpretation data were found. Nothing to combine.[/bold yellow]")
        cache = load_cache(cache_path)
        save_cache(cache_path, cache)
        return
        
    console.print(f"Loaded [green]{len(processors)}[/green] papers containing interpreted table data.")
    
    # 4. Run homogenisation data pipeline
    start_time = time.time()
    ai_instance = AI.get_instance()
    selected_model = ai_instance.selected_model

    
    combine_tree = Tree(f"[bold magenta]Homogenising Chemical Names using {selected_model}[/bold magenta]")
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}[/bold cyan]"),
        BarColumn(),
        TaskProgressColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console
    )
    task_id = progress.add_task("Homogenising papers...", total=len(processors))
    group = Group(progress, combine_tree)
    
    results = None
    with Live(group, console=console, auto_refresh=True, refresh_per_second=12):
        for event in load_and_homogenise(processors, cache_path, ai_instance):
            status = event.get("status")
            if status == "paper_start":
                paper_name = event["paper_name"]
                progress.update(task_id, description=f"Homogenising [cyan]{paper_name}[/cyan]...")
            elif status == "paper_complete":
                paper_name = event["paper_name"]
                mh_cnt = event.get("mh_count", 0)
                flory_cnt = event.get("flory_count", 0)
                combine_tree.add(
                    f"[green]✓[/green] [bold]{paper_name}[/bold] "
                    f"[dim]({flory_cnt} Flory, {mh_cnt} Mark-Houwink)[/dim]"
                )
                progress.advance(task_id)
            elif status == "complete":
                results = event["results"]
                progress.update(task_id, description="[bold green]Homogenisation complete![/bold green]")
                
    combine_elapsed = time.time() - start_time
    combine_end_time = time.time()
    
    import platform
    
    # Resolve process summary and timing details if available
    if not process_manifest:
        summary_path = os.path.join(input_dir, "process_summary.json")
        if not os.path.isfile(summary_path):
            summary_path = os.path.join(input_dir, "process_manifest.json")
        if os.path.isfile(summary_path):
            try:
                with open(summary_path, "r", encoding="utf-8") as f:
                    process_manifest = json.load(f)
            except Exception:
                process_manifest = None

    process_start_time_str = "N/A"
    process_end_time_str = "N/A"
    papers_duration_val = None

    if process_manifest:
        process_start_time_str = process_manifest.get("start_time", "N/A")
        if "end_papers_time" in process_manifest:
            process_end_time_str = process_manifest["end_papers_time"]
        elif "end_papers_timestamp" in process_manifest:
            process_end_time_str = datetime.fromtimestamp(process_manifest["end_papers_timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        elif "start_timestamp" in process_manifest and "papers_duration_seconds" in process_manifest:
            try:
                end_ts = process_manifest["start_timestamp"] + float(process_manifest["papers_duration_seconds"])
                process_end_time_str = datetime.fromtimestamp(end_ts).strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                process_end_time_str = "N/A"

        papers_sec = process_manifest.get("papers_duration_seconds")
        if isinstance(papers_sec, (int, float)):
            papers_duration_val = float(papers_sec)
        elif isinstance(papers_sec, str):
            try:
                papers_duration_val = float(papers_sec.strip().rstrip("s"))
            except ValueError:
                papers_duration_val = None

    combine_start_time_str = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
    combine_end_time_str = datetime.fromtimestamp(combine_end_time).strftime("%Y-%m-%d %H:%M:%S")
    combine_duration_val = float(combine_elapsed)

    if papers_duration_val is not None:
        total_execution_val = papers_duration_val + combine_duration_val
    else:
        total_execution_val = combine_duration_val

    papers_summary = results.get("papers_summary", [])
    total_tables_checked = sum(p.get("total_tables", 0) for p in papers_summary)
    total_tables_selected = sum(p.get("selected_tables", 0) for p in papers_summary)

    results["run_info"] = {
        "process_start_time": process_start_time_str,
        "process_end_time": process_end_time_str,
        "combine_start_time": combine_start_time_str,
        "combine_end_time": combine_end_time_str,
        "start_time": process_start_time_str if process_start_time_str != "N/A" else combine_start_time_str,
        "end_time": combine_end_time_str,
        "duration_seconds": f"{total_execution_val:.2f}s",
        "total_execution_seconds": total_execution_val,
        "papers_duration_seconds": f"{papers_duration_val:.2f}s" if papers_duration_val is not None else "N/A",
        "combine_duration_seconds": f"{combine_duration_val:.2f}s",
        "model_used": selected_model,
        "input_directory": input_dir,
        "total_papers_inputted": len(valid_subfolders),
        "num_papers": len(processors),
        "total_tables": total_tables_checked,
        "selected_tables": total_tables_selected,
        "os": f"{platform.system()} {platform.release()}",
        "architecture": platform.machine(),
        "cpu_cores": os.cpu_count() or 1,
        "python_version": sys.version.split()[0],
        "node_hostname": platform.node()
    }

    # Build flat (unaggregated) pandas dataframes and export
    df_flory, df_mh = build_flat_databases(results)
    
    # 5. Write outputs
    try:
        # Create output folders if they do not exist
        out_dir = os.path.dirname(json_out)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
            
        with open(json_out, 'w', encoding='utf-8') as jf:
            json.dump(results, jf, indent=2, ensure_ascii=False)
            
        # Save flat databases to file system
        df_flory.to_pickle(f"{output_prefix}_flory_database.pkl")
        df_flory.to_csv(f"{output_prefix}_flory_database.csv", index=False)
        df_mh.to_pickle(f"{output_prefix}_mh_database.pkl")
        df_mh.to_csv(f"{output_prefix}_mh_database.csv", index=False)
            
        create_combined_excel(xlsx_out, results)
        
        # Generate publication-ready matplotlib charts in plots subfolder
        plots_out_dir = out_dir if out_dir else input_dir
        generated_plots = create_plots(plots_out_dir, results)
        
    except Exception as e:
        console.print(f"[bold red]Error saving outputs: {e}[/bold red]")
        sys.exit(1)
        
    # Sort papers and copy PDFs into sorted/healthy, sorted/unhealthy, sorted/noData
    sort_counts = sort_and_save(processors, input_dir, results=results, pdf_dir=pdf_dir)

    # 6. Report results and statistics
    console.print()
    run_info = results.get("run_info", {})
    from chemstractor.lib.reports.helpers import format_duration
    if run_info.get("papers_duration_seconds") and run_info.get("papers_duration_seconds") != "N/A":
        console.print(
            f"[bold green]✓[/bold green] Combining process completed in [yellow]{format_duration(combine_duration_val)}[/yellow] "
            f"(Total execution time: [yellow]{format_duration(total_execution_val)}[/yellow], Papers: [yellow]{format_duration(papers_duration_val)}[/yellow])."
        )
    else:
        console.print(f"[bold green]✓[/bold green] Combining process completed in [yellow]{format_duration(combine_duration_val)}[/yellow].")
    console.print(f"JSON data saved to: [cyan]{json_out}[/cyan]")
    console.print(f"Excel report saved to: [cyan]{xlsx_out}[/cyan]")
    if generated_plots:
        plots_folder = os.path.dirname(generated_plots[0])
        console.print(f"Matplotlib plots saved to: [cyan]{plots_folder}[/cyan] ({len(generated_plots)} PNG charts generated)")
    console.print(f"Flory database saved to: [cyan]{output_prefix}_flory_database.pkl / .csv[/cyan]")
    console.print(f"Mark-Houwink database saved to: [cyan]{output_prefix}_mh_database.pkl / .csv[/cyan]")
    sorted_dir = os.path.join(input_dir, "sorted")
    console.print(f"Sorted paper PDFs saved to: [cyan]{sorted_dir}[/cyan]")
    console.print(f"  - Healthy: [green]{sort_counts.get('healthy', 0)}[/green]")
    console.print(f"  - Unhealthy: [yellow]{sort_counts.get('unhealthy', 0)}[/yellow]")
    console.print(f"  - No Data: [dim]{sort_counts.get('noData', 0)}[/dim]")
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
    
    failed_entries_all = []
    for e in results.get("flory_entries", []):
        if is_entry_failed(e):
            failed_entries_all.append(("Flory", e))
    for e in results.get("mark_houwink_entries", []):
        if is_entry_failed(e):
            failed_entries_all.append(("Mark-Houwink", e))

    if failed_entries_all:
        console.print()
        console.print(f"[bold yellow]Recorded Entry Failures ({len(failed_entries_all)}):[/bold yellow]")
        for entry_type, entry in failed_entries_all[:15]:
            ff = entry.get("failed_fields", {})
            err_keys = [k for k, v in ff.items() if v] if isinstance(ff, dict) else ["failed"]
            console.print(f" - [dim]{entry.get('source_paper')}/{entry.get('table_name')}[/dim] ({entry_type}): Active Errors [red]{', '.join(err_keys)}[/red]")
        if len(failed_entries_all) > 15:
            console.print(f" ... and {len(failed_entries_all) - 15} more failed entries. See the Failures sheet in Excel.")
            
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
