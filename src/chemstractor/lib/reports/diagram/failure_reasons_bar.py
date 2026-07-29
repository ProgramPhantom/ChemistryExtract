import os
import matplotlib.pyplot as plt

def generate_failure_reasons_bar_chart(plots_dir: str, failure_reasons_count: dict) -> str | None:
    """Generates horizontal bar chart breaking down failure reasons."""
    if not failure_reasons_count:
        return None

    try:
        fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
        sorted_reasons = sorted(failure_reasons_count.items(), key=lambda x: x[1])
        reasons = [r[0] for r in sorted_reasons]
        val_counts = [r[1] for r in sorted_reasons]
        
        bars = ax.barh(reasons, val_counts, color="#dd6b20", height=0.55, edgecolor="#c05621", linewidth=0.8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_xlabel("Count of Failures")
        ax.set_title("Failure Reasons Breakdown", pad=12)
        ax.xaxis.grid(True, linestyle="--", alpha=0.5, color="#cbd5e0")
        ax.set_axisbelow(True)
        
        max_c = max(val_counts) if val_counts else 1
        for bar in bars:
            w = bar.get_width()
            ax.text(w + max_c * 0.015, bar.get_y() + bar.get_height() / 2,
                    f"{int(w)}", va="center", ha="left", fontsize=9.5, fontweight="bold", color="#2d3748")
            
        p2 = os.path.join(plots_dir, "summary_failure_reasons.png")
        fig.savefig(p2, bbox_inches="tight")
        plt.close(fig)
        return p2
    except Exception:
        pass
    return None
