import os
import plotly.graph_objects as go
from chemstractor.lib.reports.helpers import ERROR_SEVERITY_MAP, is_entry_failed

def generate_flory_sankey_diagram(plots_dir: str, combined_data: dict) -> list[str]:
    """Generates interactive HTML and static PNG Plotly Sankey diagram for Flory entries processing flow."""
    generated = []
    try:
        flory_entries = combined_data.get("flory_entries", [])
        run_info = combined_data.get("run_info", {})
        papers_summary = combined_data.get("papers_summary", [])
        
        num_input_pdfs = run_info.get("total_papers_inputted")
        if num_input_pdfs is None or num_input_pdfs <= 0:
            num_input_pdfs = len(papers_summary) if papers_summary else (
                len(set(e.get("source_paper") for e in flory_entries if e.get("source_paper"))) or 1
            )
            
        num_flory_rows = len(flory_entries)
        
        # Categorize Flory rows into error-free vs specific errors
        flory_error_free = 0
        flory_error_counts = {}
        
        for entry in flory_entries:
            if not is_entry_failed(entry):
                flory_error_free += 1
            else:
                ff = entry.get("failed_fields", "None")
                poly = entry.get("polymer_name", "")
                solv = entry.get("solvent", "")
                
                active_reasons = []
                if isinstance(ff, dict):
                    for f_key, is_failed in ff.items():
                        if is_failed:
                            lbl = ERROR_SEVERITY_MAP.get(f_key, {}).get("label", f_key)
                            active_reasons.append(lbl)
                elif isinstance(ff, str) and ff != "None":
                    for item in ff.split(","):
                        item_clean = item.strip()
                        if item_clean and item_clean != "None":
                            lbl = ERROR_SEVERITY_MAP.get(item_clean, {}).get("label", item_clean)
                            active_reasons.append(lbl)
                            
                if not active_reasons:
                    if poly in (None, "N/A"):
                        active_reasons.append(ERROR_SEVERITY_MAP.get("polymer_name", {}).get("label", "Polymer Identification Failure"))
                    if solv in (None, "N/A"):
                        active_reasons.append(ERROR_SEVERITY_MAP.get("solvent_name", {}).get("label", "Solvent Identification Failure"))
                        
                if not active_reasons:
                    active_reasons.append("Unspecified Flory Entry Error")
                    
                for r in active_reasons:
                    flory_error_counts[r] = flory_error_counts.get(r, 0) + 1

        # Node setup for Sankey:
        # Layer 1: Node 0 = Input PDF Files
        # Layer 2: Node 1 = Flory Marked Rows
        # Layer 3: Node 2 = Error Free, Node 3..K = Error reasons
        node_labels = [
            f"Input PDF Files ({num_input_pdfs})",
            f"Flory Marked Rows ({num_flory_rows})"
        ]
        node_colors = [
            "#2b6cb0",  # Layer 1: Input PDFs (Deep Blue)
            "#6b46c1"   # Layer 2: Flory Marked Rows (Purple)
        ]
        
        sources = []
        targets = []
        values = []
        link_colors = []
        
        # Link Layer 1 -> Layer 2
        if num_flory_rows > 0:
            sources.append(0)
            targets.append(1)
            values.append(num_flory_rows)
            link_colors.append("rgba(43, 108, 176, 0.4)")
            
        # Add Layer 3 nodes & links from Layer 2
        if flory_error_free > 0:
            node_idx = len(node_labels)
            node_labels.append(f"Error Free ({flory_error_free})")
            node_colors.append("#2f855a")  # Green
            
            sources.append(1)
            targets.append(node_idx)
            values.append(flory_error_free)
            link_colors.append("rgba(47, 133, 90, 0.4)")
            
        fail_palette_rgba = [
            ("rgba(229, 62, 62, 0.5)", "#e53e3e"),
            ("rgba(221, 107, 32, 0.5)", "#dd6b20"),
            ("rgba(214, 158, 46, 0.5)", "#d69e2e"),
            ("rgba(128, 90, 213, 0.5)", "#805ad5"),
            ("rgba(197, 48, 48, 0.5)", "#c53030"),
            ("rgba(183, 121, 31, 0.5)", "#b7791f"),
            ("rgba(155, 44, 44, 0.5)", "#9b2c2c")
        ]
        
        if flory_error_counts:
            sorted_errors = sorted(flory_error_counts.items(), key=lambda x: x[1], reverse=True)
            for idx, (reason, count) in enumerate(sorted_errors):
                node_idx = len(node_labels)
                node_labels.append(f"Fail: {reason} ({count})")
                
                rgba, hex_col = fail_palette_rgba[idx % len(fail_palette_rgba)]
                node_colors.append(hex_col)
                
                sources.append(1)
                targets.append(node_idx)
                values.append(count)
                link_colors.append(rgba)
                
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=18,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=node_labels,
                color=node_colors
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                color=link_colors
            )
        )])
        
        fig.update_layout(
            title_text="<b>Flory Coefficients Extraction Flow & Error Breakdown</b>",
            font_size=12,
            font_family="DejaVu Sans, Arial, sans-serif",
            width=900,
            height=600
        )
        
        html_path = os.path.join(plots_dir, "flory_sankey_diagram.html")
        fig.write_html(html_path)
        generated.append(html_path)
        
        try:
            png_path = os.path.join(plots_dir, "flory_sankey_diagram.png")
            fig.write_image(png_path, scale=2)
            generated.append(png_path)
        except Exception:
            pass

    except Exception:
        pass

    return generated
