import os
import matplotlib.pyplot as plt

def generate_success_rate_pie_chart(
    plots_dir: str,
    total_collected: int,
    total_successes: int,
    total_failures_all: int,
    failure_reasons_count: dict
) -> str | None:
    """Generates the extraction and interpretation success rate & error breakdown donut chart."""
    if total_collected <= 0:
        return None

    try:
        fig, ax = plt.subplots(figsize=(8.0, 5.5), dpi=300)
        
        pie_counts = []
        pie_labels = []
        pie_colors = []
        
        # Success category
        if total_successes > 0:
            pie_counts.append(total_successes)
            pie_labels.append(f"Successful ({total_successes})")
            pie_colors.append("#2b6cb0")  # Deep blue for success
            
        # Failure categories broken down by reason
        fail_palette = ["#e53e3e", "#dd6b20", "#d69e2e", "#805ad5", "#c53030", "#b7791f", "#9b2c2c", "#742a2a"]
        
        if failure_reasons_count:
            sorted_reasons = sorted(failure_reasons_count.items(), key=lambda x: x[1], reverse=True)
            for idx, (reason, count) in enumerate(sorted_reasons):
                pie_counts.append(count)
                pie_labels.append(f"Fail: {reason} ({count})")
                pie_colors.append(fail_palette[idx % len(fail_palette)])
        elif total_failures_all > 0:
            pie_counts.append(total_failures_all)
            pie_labels.append(f"Failed ({total_failures_all})")
            pie_colors.append("#e53e3e")

        if sum(pie_counts) > 0:
            def autopct_format(pct):
                return f"{pct:.1f}%" if pct >= 3.0 else ""

            wedges, texts, autotexts = ax.pie(
                pie_counts,
                autopct=autopct_format,
                startangle=140,
                colors=pie_colors,
                wedgeprops=dict(width=0.4, edgecolor="white", linewidth=1.5),
                pctdistance=0.75
            )
            for autotext in autotexts:
                autotext.set_color("white")
                autotext.set_weight("bold")
                autotext.set_fontsize(9.5)
                
            success_rate = (total_successes / total_collected * 100) if total_collected > 0 else 0
            ax.text(
                0, 0, f"Success Rate\n{success_rate:.1f}%",
                ha="center", va="center", fontsize=12, fontweight="bold", color="#1a202c"
            )
            ax.set_title("Extraction & Interpretation Success Rate & Error Breakdown", pad=15)
            ax.legend(
                wedges, pie_labels,
                title="Outcome / Failure Reason",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1),
                frameon=True,
                facecolor="#f7fafc",
                edgecolor="#e2e8f0",
                fontsize=9
            )
            
            p1 = os.path.join(plots_dir, "summary_success_rate.png")
            fig.savefig(p1, bbox_inches="tight")
            plt.close(fig)
            return p1
        plt.close(fig)
    except Exception:
        pass
    return None
