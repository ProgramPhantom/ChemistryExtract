import os
import matplotlib.pyplot as plt
from chemstractor.lib.reports.helpers import is_entry_failed

COLOR_PALETTE = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#319795", "#d69e2e", "#805ad5", "#dd6b20", "#3182ce"
]

def generate_flory_calibration_plot(plots_dir: str, flory_entries: list) -> str | None:
    """Generates Flory Calibration Curves log-log plot."""
    if not flory_entries:
        return None

    try:
        fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=300)
        valid_flory_idx = 0
        
        x_vals = [3, 6]
        for idx, entry in enumerate(flory_entries):
            c_val = entry.get("c_value")
            v_val = entry.get("v_value")
            has_failed = is_entry_failed(entry)
            if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)) and not has_failed:
                y3 = c_val - v_val * 3
                y6 = c_val - v_val * 6
                
                label = f"{entry.get('polymer_name')} in {entry.get('solvent')}"
                color = COLOR_PALETTE[valid_flory_idx % len(COLOR_PALETTE)]
                
                ax.plot(x_vals, [y3, y6], label=label, color=color,
                        linewidth=2.0, alpha=0.9)
                valid_flory_idx += 1
                
        if valid_flory_idx > 0:
            ax.set_title("Flory Calibration Curves (log-log Plot)", pad=12)
            ax.set_xlabel(r"$\log_{10}(M\ /\ \mathrm{g\ mol^{-1}})$")
            ax.set_ylabel(r"$\log_{10}(D\ /\ \mathrm{m^2\ s^{-1}})$")
            ax.set_xticks([3, 4, 5, 6])
            ax.grid(True, linestyle="--", alpha=0.6, color="#cbd5e0")
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            
            ax.legend(
                bbox_to_anchor=(1.04, 1), loc="upper left",
                frameon=True, facecolor="#f7fafc", edgecolor="#e2e8f0", fontsize=8.5
            )
            
            p3 = os.path.join(plots_dir, "flory_calibration_curves.png")
            fig.savefig(p3, bbox_inches="tight")
            plt.close(fig)
            return p3
        plt.close(fig)
    except Exception:
        pass
    return None
