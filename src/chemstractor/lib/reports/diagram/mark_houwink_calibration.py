import os
import math
import matplotlib.pyplot as plt
from chemstractor.lib.reports.helpers import is_entry_failed

COLOR_PALETTE = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#319795", "#d69e2e", "#805ad5", "#dd6b20", "#3182ce"
]

def generate_mark_houwink_calibration_plot(plots_dir: str, mh_entries: list) -> str | None:
    """Generates Mark-Houwink Calibration Curves log-log plot."""
    if not mh_entries:
        return None

    try:
        fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=300)
        valid_mh_idx = 0
        
        x_vals = [3, 6]
        for idx, entry in enumerate(mh_entries):
            K_val = entry.get("K_value")
            a_val = entry.get("a_value")
            has_failed = is_entry_failed(entry)
            if isinstance(K_val, (int, float)) and K_val > 0 and isinstance(a_val, (int, float)) and not has_failed:
                log_K = math.log10(K_val)
                y3 = log_K + a_val * 3
                y6 = log_K + a_val * 6
                
                label = f"{entry.get('polymer_name')} in {entry.get('solvent')}"
                color = COLOR_PALETTE[valid_mh_idx % len(COLOR_PALETTE)]
                
                ax.plot(x_vals, [y3, y6], label=label, color=color,
                        linewidth=2.0, alpha=0.9)
                valid_mh_idx += 1
                
        if valid_mh_idx > 0:
            ax.set_title("Mark-Houwink Calibration Curves (log-log Plot)", pad=12)
            ax.set_xlabel(r"$\log_{10}(M\ /\ \mathrm{g\ mol^{-1}})$")
            ax.set_ylabel(r"$\log_{10}([\eta]\ /\ \mathrm{mL\ g^{-1}})$")
            ax.set_xticks([3, 4, 5, 6])
            ax.grid(True, linestyle="--", alpha=0.6, color="#cbd5e0")
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            
            ax.legend(
                bbox_to_anchor=(1.04, 1), loc="upper left",
                frameon=True, facecolor="#f7fafc", edgecolor="#e2e8f0", fontsize=8.5
            )
            
            p4 = os.path.join(plots_dir, "mark_houwink_calibration_curves.png")
            fig.savefig(p4, bbox_inches="tight")
            plt.close(fig)
            return p4
        plt.close(fig)
    except Exception:
        pass
    return None
