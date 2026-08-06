import os
import plotly.graph_objects as go  # type: ignore
from chemstractor.lib.reports.helpers import ERROR_SEVERITY_MAP, is_entry_failed

def generate_flory_sankey_diagram(plots_dir: str, combined_data: dict) -> list[str]:
    """Generates interactive HTML and static PNG Plotly Sankey diagram for Flory entries processing flow."""
    generated = []
    try:
        flory_entries = combined_data.get("flory_entries", [])
        run_info = combined_data.get("run_info", {})
        papers_summary = combined_data.get("papers_summary", [])
        
        num_input_pdfs = run_info.get("total_papers_inputted")
        num_selected_papers = run_info.get("num_papers")
        
        if num_selected_papers is None or num_selected_papers < 0:
            num_selected_papers = len(papers_summary) if papers_summary else (
                len(set(e.get("source_paper") for e in flory_entries if e.get("source_paper")))
            )

        if num_input_pdfs is None or num_input_pdfs <= 0:
            num_input_pdfs = len(papers_summary) if papers_summary else (
                len(set(e.get("source_paper") for e in flory_entries if e.get("source_paper"))) or 1
            )
            
        if num_input_pdfs < num_selected_papers:
            num_input_pdfs = num_selected_papers

        num_unselected_pdfs = max(0, num_input_pdfs - num_selected_papers)
        num_flory_rows = len(flory_entries)
        
        # Categorize Flory rows:
        # 1. Final Selected Entries (entries with NO deselected or problem errors)
        # 2. Deselected errors (entries/reasons with "deselected" severity)
        # 3. Problem errors (entries/reasons with "problem" severity)
        # Note: "warning" severity errors (e.g. temperature_missing) are EXCLUDED completely.
        num_passed_selection = 0
        deselected_error_counts = {}
        problem_error_counts = {}

        for entry in flory_entries:
            if not is_entry_failed(entry):
                num_passed_selection += 1
            else:
                ff = entry.get("failed_fields", "None")
                poly = entry.get("polymer_name", "")
                solv = entry.get("solvent_name", entry.get("solvent", ""))

                active_reasons = []
                if isinstance(ff, dict):
                    for f_key, is_failed in ff.items():
                        if is_failed:
                            meta = ERROR_SEVERITY_MAP.get(f_key, {})
                            severity = meta.get("severity", "problem")
                            if severity == "warning":
                                continue
                            lbl = meta.get("label", f_key)
                            active_reasons.append((severity, lbl))
                elif isinstance(ff, str) and ff != "None":
                    for item in ff.split(","):
                        item_clean = item.strip()
                        if item_clean and item_clean != "None":
                            meta = ERROR_SEVERITY_MAP.get(item_clean, {})
                            severity = meta.get("severity", "problem")
                            if severity == "warning":
                                continue
                            lbl = meta.get("label", item_clean)
                            active_reasons.append((severity, lbl))

                if not active_reasons:
                    if poly in (None, "", "N/A", "Invalid chemical"):
                        lbl = ERROR_SEVERITY_MAP.get("polymer_name", {}).get("label", "Polymer Identification Failure")
                        active_reasons.append(("deselected", lbl))
                    if solv in (None, "", "N/A", "Invalid chemical"):
                        lbl = ERROR_SEVERITY_MAP.get("solvent_name", {}).get("label", "Solvent Identification Failure")
                        active_reasons.append(("deselected", lbl))

                if not active_reasons:
                    active_reasons.append(("problem", "Unspecified Flory Entry Error"))

                for severity, lbl in active_reasons:
                    if severity == "deselected":
                        deselected_error_counts[lbl] = deselected_error_counts.get(lbl, 0) + 1
                    elif severity == "problem":
                        problem_error_counts[lbl] = problem_error_counts.get(lbl, 0) + 1

        # Node setup for Sankey:
        # Layer 1: Node 0 = Input PDF Files
        # Layer 2: Node 1 = Selected PDF Files, (Optional Node 2 = PDF Files Not Selected)
        # Layer 3: Flory Marked Rows
        # Layer 4: Severity Level Nodes: Final Selected Entries, Deselected, Problem
        # Layer 5: Specific error nodes under Deselected & Problem
        node_labels = [
            f"Input PDF Files ({num_input_pdfs})",
            f"Selected PDF Files ({num_selected_papers})"
        ]
        node_colors = [
            "#2b6cb0",  # Layer 1: Input PDFs (Deep Blue)
            "#3182ce"   # Layer 2: Selected PDF Files (Blue)
        ]

        sources = []
        targets = []
        values = []
        link_colors = []

        # Optional Node for PDF Files Not Selected
        if num_unselected_pdfs > 0:
            unselected_node_idx = len(node_labels)
            node_labels.append(f"PDF Files Not Selected ({num_unselected_pdfs})")
            node_colors.append("#a0aec0")  # Slate Gray

            sources.append(0)
            targets.append(unselected_node_idx)
            values.append(num_unselected_pdfs)
            link_colors.append("rgba(160, 174, 192, 0.4)")

        # Link Layer 1 -> Layer 2 (Input -> Selected)
        if num_selected_papers > 0:
            sources.append(0)
            targets.append(1)
            values.append(num_selected_papers)
            link_colors.append("rgba(43, 108, 176, 0.4)")

        # Flory Marked Rows Node
        flory_node_idx = len(node_labels)
        node_labels.append(f"Flory Marked Rows ({num_flory_rows})")
        node_colors.append("#6b46c1")  # Layer 3: Flory Marked Rows (Purple)

        # Link Selected PDF Files -> Flory Marked Rows
        if num_flory_rows > 0:
            sources.append(1)
            targets.append(flory_node_idx)
            values.append(num_flory_rows)
            link_colors.append("rgba(49, 130, 206, 0.4)")

        # Layer 4: Final Selected Entries (Passed Selection)
        if num_passed_selection > 0:
            node_idx = len(node_labels)
            node_labels.append(f"Final Selected Entries ({num_passed_selection})")
            node_colors.append("#2f855a")  # Green

            sources.append(flory_node_idx)
            targets.append(node_idx)
            values.append(num_passed_selection)
            link_colors.append("rgba(47, 133, 90, 0.4)")

        # Layer 4: Deselected Node
        total_deselected = sum(deselected_error_counts.values())
        deselected_node_idx = None
        if total_deselected > 0:
            deselected_node_idx = len(node_labels)
            node_labels.append(f"Deselected ({total_deselected})")
            node_colors.append("#c53030")  # Crimson Red

            sources.append(flory_node_idx)
            targets.append(deselected_node_idx)
            values.append(total_deselected)
            link_colors.append("rgba(197, 48, 48, 0.4)")

        # Layer 4: Problem Node
        total_problem = sum(problem_error_counts.values())
        problem_node_idx = None
        if total_problem > 0:
            problem_node_idx = len(node_labels)
            node_labels.append(f"Problem ({total_problem})")
            node_colors.append("#dd6b20")  # Dark Orange

            sources.append(flory_node_idx)
            targets.append(problem_node_idx)
            values.append(total_problem)
            link_colors.append("rgba(221, 107, 32, 0.4)")

        # Layer 5: Specific Deselected Error Nodes
        if deselected_node_idx is not None and deselected_error_counts:
            deselected_palette = [
                ("rgba(229, 62, 62, 0.5)", "#e53e3e"),
                ("rgba(155, 44, 44, 0.5)", "#9b2c2c"),
                ("rgba(197, 48, 48, 0.5)", "#c53030")
            ]
            sorted_deselected = sorted(deselected_error_counts.items(), key=lambda x: x[1], reverse=True)
            for idx, (reason, count) in enumerate(sorted_deselected):
                node_idx = len(node_labels)
                node_labels.append(f"{reason} ({count})")
                rgba, hex_col = deselected_palette[idx % len(deselected_palette)]
                node_colors.append(hex_col)

                sources.append(deselected_node_idx)
                targets.append(node_idx)
                values.append(count)
                link_colors.append(rgba)

        # Layer 5: Specific Problem Error Nodes
        if problem_node_idx is not None and problem_error_counts:
            problem_palette = [
                ("rgba(221, 107, 32, 0.5)", "#dd6b20"),
                ("rgba(214, 158, 46, 0.5)", "#d69e2e"),
                ("rgba(183, 121, 31, 0.5)", "#b7791f"),
                ("rgba(128, 90, 213, 0.5)", "#805ad5"),
                ("rgba(202, 138, 4, 0.5)", "#ca8a04")
            ]
            sorted_problem = sorted(problem_error_counts.items(), key=lambda x: x[1], reverse=True)
            for idx, (reason, count) in enumerate(sorted_problem):
                node_idx = len(node_labels)
                node_labels.append(f"{reason} ({count})")
                rgba, hex_col = problem_palette[idx % len(problem_palette)]
                node_colors.append(hex_col)

                sources.append(problem_node_idx)
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
            title_text="<b>Flory Coefficients Extraction Problem Breakdown</b>",
            font_size=12,
            font_family="Helvetica, Arial, sans-serif",
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
