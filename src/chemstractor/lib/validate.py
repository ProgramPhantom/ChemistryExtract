import math
import typing

# =============================================================================
# Customisable Flory Parameter Validation Bounds
# =============================================================================
FLORY_V_MIN = 0.33
FLORY_V_MAX = 1.0

FLORY_D_CENTER = -9.0
FLORY_D_TOLERANCE = 6.0
FLORY_D_MIN = FLORY_D_CENTER - FLORY_D_TOLERANCE  # -15.0
FLORY_D_MAX = FLORY_D_CENTER + FLORY_D_TOLERANCE  # -3.0

# =============================================================================
# Customisable Mark-Houwink Parameter Validation Bounds
# =============================================================================
MH_A_MIN = 0.4
MH_A_MAX = 1.2

MH_K_MIN = 1e-8
MH_K_MAX = 1.0

MH_LOG_ETA_MIN = -6.0
MH_LOG_ETA_MAX = 6.0


def compute_flory_d_value(c_value: float, v_value: float, log_m: float = 3.0) -> float:
    """Computes the D value (hydrodynamic scaling) for a given log10(M) from Flory parameters c and v."""
    return c_value - v_value * log_m


def compute_flory_d_values(c_value: float, v_value: float, log_m_list: list[float] = (3.0, 6.0)) -> list[float]:
    """Computes D values for a list of log10(M) values."""
    return [compute_flory_d_value(c_value, v_value, m) for m in log_m_list]




def validate_flory_entry(
    entry: dict,
    paper_name: str = "",
    table_name: str = "",
    failures: list = None
) -> dict[str, str]:
    """
    Validates numerical Flory coefficients (v_value and calculated D values).
    Attaches 'Out of range' error to failures list if any coefficient is out of bounds.
    Returns a dict mapping failed field name -> 'Out of range'.
    """
    failed_fields = {}

    # Check v_value range
    v_val = entry.get("v_value")
    if isinstance(v_val, (int, float)):
        if not (FLORY_V_MIN <= abs(v_val) <= FLORY_V_MAX):
            failed_fields["v_value"] = "Out of range"
            if failures is not None:
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "v_value",
                    "value": str(v_val),
                    "reason": "Out of range"
                })

    # Check D values calculated from c_value and v_value
    c_val = entry.get("c_value")
    if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)):
        try:
            d_vals = compute_flory_d_values(c_val, v_val)
            for d in d_vals:
                if not (FLORY_D_MIN <= d <= FLORY_D_MAX):
                    if "general_err" not in failed_fields:
                        failed_fields["general_err"] = "D out of range"
                        if failures is not None:
                            failures.append({
                                "source_paper": paper_name,
                                "table": table_name,
                                "field": "general_err",
                                "value": f"D={d:.2f}",
                                "reason": "D out of range"
                            })
                    break
        except Exception:
            pass

    return failed_fields



def compute_mh_log_eta_value(k_value: float, a_value: float, log_m: float = 3.0) -> float:
    """Computes log10([eta]) for a given log10(M) from Mark-Houwink parameters K and a."""
    if k_value <= 0:
        raise ValueError("K_value must be positive")
    return math.log10(k_value) + a_value * log_m


def compute_mh_log_eta_values(k_value: float, a_value: float, log_m_list: list[float] = (3.0, 6.0)) -> list[float]:
    """Computes log10([eta]) values for a list of log10(M) values."""
    return [compute_mh_log_eta_value(k_value, a_value, m) for m in log_m_list]


def validate_mark_houwink_entry(
    entry: dict,
    paper_name: str = "",
    table_name: str = "",
    failures: list = None
) -> dict[str, str]:
    """
    Validates numerical Mark-Houwink coefficients (a_value, K_value, and calculated log10([eta])).
    Attaches 'Out of range' error to failures list if any coefficient is out of bounds.
    Returns a dict mapping failed field name -> 'Out of range'.
    """
    failed_fields = {}

    # Check a_value range
    a_val = entry.get("a_value")
    if isinstance(a_val, (int, float)):
        if not (MH_A_MIN <= a_val <= MH_A_MAX):
            failed_fields["a_value"] = "Out of range"
            if failures is not None:
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "a_value",
                    "value": str(a_val),
                    "reason": "Out of range"
                })

    # Check K_value range
    k_val = entry.get("K_value")
    if isinstance(k_val, (int, float)):
        if not (MH_K_MIN <= k_val <= MH_K_MAX):
            failed_fields["K_value"] = "Out of range"
            if failures is not None:
                failures.append({
                    "source_paper": paper_name,
                    "table": table_name,
                    "field": "K_value",
                    "value": str(k_val),
                    "reason": "Out of range"
                })

    # Check computed log10([eta]) values
    if isinstance(k_val, (int, float)) and isinstance(a_val, (int, float)) and k_val > 0:
        try:
            log_eta_vals = compute_mh_log_eta_values(k_val, a_val)
            for log_eta in log_eta_vals:
                if not (MH_LOG_ETA_MIN <= log_eta <= MH_LOG_ETA_MAX):
                    if "general_err" not in failed_fields:
                        failed_fields["general_err"] = "Out of range"
                        if failures is not None:
                            failures.append({
                                "source_paper": paper_name,
                                "table": table_name,
                                "field": "general_err",
                                "value": f"log_eta={log_eta:.2f}",
                                "reason": "Out of range"
                            })
                    break
        except Exception:
            pass

    return failed_fields
