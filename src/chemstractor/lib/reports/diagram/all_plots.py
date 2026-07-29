import os
import matplotlib.pyplot as plt
from chemstractor.lib.reports.helpers import ERROR_SEVERITY_MAP, is_entry_failed
from chemstractor.lib.reports.diagram.success_rate_pie import generate_success_rate_pie_chart
from chemstractor.lib.reports.diagram.failure_reasons_bar import generate_failure_reasons_bar_chart
from chemstractor.lib.reports.diagram.flory_calibration import generate_flory_calibration_plot
from chemstractor.lib.reports.diagram.mark_houwink_calibration import generate_mark_houwink_calibration_plot
from chemstractor.lib.reports.diagram.flory_sankey import generate_flory_sankey_diagram

def create_plots(output_dir: str, combined_data: dict) -> list[str]:
    """Generates publication-quality Matplotlib charts and Plotly Sankey diagrams into a 'plots' subfolder under output_dir."""
    plots_dir = os.path.join(output_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    
    generated_plots = []
    
    # Publication-ready matplotlib aesthetic settings
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica", "sans-serif"],
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.labelweight": "medium",
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.fontsize": 9,
        "figure.titlesize": 13,
        "axes.edgecolor": "#2d3748",
        "axes.linewidth": 1.0,
        "grid.color": "#e2e8f0",
        "grid.linestyle": "--",
        "grid.alpha": 0.7,
        "savefig.dpi": 300,
        "savefig.bbox": "tight"
    })
    
    flory_entries = combined_data.get("flory_entries", [])
    mh_entries = combined_data.get("mark_houwink_entries", [])
    failures = combined_data.get("failures", [])
    
    # Pre-calculate failure stats for Summary plots
    failure_reasons_count = {}
    total_mh_failed = 0
    for entry in mh_entries:
        ff = entry.get("failed_fields", "None")
        poly = entry.get("polymer_name", "")
        solv = entry.get("solvent_name", entry.get("solvent", ""))
        if isinstance(ff, dict):
            if is_entry_failed(entry):
                total_mh_failed += 1
                for f_key, is_failed in ff.items():
                    if is_failed:
                        lbl = ERROR_SEVERITY_MAP.get(f_key, {}).get("label", f_key)
                        failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif isinstance(ff, str) and ff != "None":
            total_mh_failed += 1
            for item in ff.split(","):
                item_clean = item.strip()
                if item_clean and item_clean != "None":
                    lbl = ERROR_SEVERITY_MAP.get(item_clean, {}).get("label", item_clean)
                    failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif is_entry_failed(entry):
            total_mh_failed += 1
            if poly in (None, "N/A"):
                failure_reasons_count["Polymer Identification Failure"] = failure_reasons_count.get("Polymer Identification Failure", 0) + 1
            if solv in (None, "N/A"):
                failure_reasons_count["Solvent Identification Failure"] = failure_reasons_count.get("Solvent Identification Failure", 0) + 1

    total_flory_failed = 0
    for entry in flory_entries:
        ff = entry.get("failed_fields", "None")
        poly = entry.get("polymer_name", "")
        solv = entry.get("solvent_name", entry.get("solvent", ""))
        if isinstance(ff, dict):
            if is_entry_failed(entry):
                total_flory_failed += 1
                for f_key, is_failed in ff.items():
                    if is_failed:
                        lbl = ERROR_SEVERITY_MAP.get(f_key, {}).get("label", f_key)
                        failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif isinstance(ff, str) and ff != "None":
            total_flory_failed += 1
            for item in ff.split(","):
                item_clean = item.strip()
                if item_clean and item_clean != "None":
                    lbl = ERROR_SEVERITY_MAP.get(item_clean, {}).get("label", item_clean)
                    failure_reasons_count[lbl] = failure_reasons_count.get(lbl, 0) + 1
        elif is_entry_failed(entry):
            total_flory_failed += 1
            if poly in (None, "N/A"):
                failure_reasons_count["Polymer Identification Failure"] = failure_reasons_count.get("Polymer Identification Failure", 0) + 1
            if solv in (None, "N/A"):
                failure_reasons_count["Solvent Identification Failure"] = failure_reasons_count.get("Solvent Identification Failure", 0) + 1

    paper_level_failures = 0
    for fail in failures:
        field = fail.get("field", "")
        reason = fail.get("reason", "Unknown failure")
        if field in ("Paper processing", "Mark-Houwink processing", "Flory processing"):
            paper_level_failures += 1
            failure_reasons_count[reason] = failure_reasons_count.get(reason, 0) + 1

    total_collected = len(flory_entries) + len(mh_entries)
    total_failures_all = total_flory_failed + total_mh_failed + paper_level_failures
    total_successes = max(0, total_collected - (total_flory_failed + total_mh_failed))

    # 1. Donut Pie Chart
    p1 = generate_success_rate_pie_chart(
        plots_dir, total_collected, total_successes, total_failures_all, failure_reasons_count
    )
    if p1:
        generated_plots.append(p1)

    # 2. Failure Reasons Bar Chart
    p2 = generate_failure_reasons_bar_chart(plots_dir, failure_reasons_count)
    if p2:
        generated_plots.append(p2)

    # 3. Flory Calibration Plot
    p3 = generate_flory_calibration_plot(plots_dir, flory_entries)
    if p3:
        generated_plots.append(p3)

    # 4. Mark-Houwink Calibration Plot
    p4 = generate_mark_houwink_calibration_plot(plots_dir, mh_entries)
    if p4:
        generated_plots.append(p4)

    # 5. Plotly Sankey Diagram
    sankey_plots = generate_flory_sankey_diagram(plots_dir, combined_data)
    for p in sankey_plots:
        generated_plots.append(p)

    return generated_plots
