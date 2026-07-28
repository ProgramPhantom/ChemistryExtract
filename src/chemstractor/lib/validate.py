import math
import typing

# =============================================================================
# Customisable Flory Parameter Validation Bounds
# =============================================================================
FLORY_V_MIN = 0.33
FLORY_V_MAX = 1.0

FLORY_D_CENTER = -9.0
FLORY_D_TOLERANCE = 3.0
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




def validate_flory_entry(entry: dict) -> dict[str, bool]:
    """
    Validates numerical Flory coefficients (v_value and calculated D values).
    Returns a dict mapping error flag name -> boolean.
    """
    failed_flags = {
        "v_value_out_of_range": False,
        "D_out_of_range": False
    }

    # Check v_value range
    v_val = entry.get("v_value")
    if isinstance(v_val, str):
        try:
            v_val = float(v_val.strip())
        except ValueError:
            pass

    if isinstance(v_val, (int, float)):
        if not (FLORY_V_MIN <= abs(v_val) <= FLORY_V_MAX):
            failed_flags["v_value_out_of_range"] = True
    elif v_val is not None:
        failed_flags["v_value_out_of_range"] = True

    # Check D values calculated from c_value and v_value
    c_val = entry.get("c_value")
    if isinstance(c_val, str):
        try:
            c_val = float(c_val.strip())
        except ValueError:
            pass

    if isinstance(c_val, (int, float)) and isinstance(v_val, (int, float)):
        try:
            d_vals = compute_flory_d_values(c_val, v_val)
            for d in d_vals:
                if not (FLORY_D_MIN <= d <= FLORY_D_MAX):
                    failed_flags["D_out_of_range"] = True
                    break
        except Exception:
            pass

    return failed_flags


def compute_mh_log_eta_value(k_value: float, a_value: float, log_m: float = 3.0) -> float:
    """Computes log10([eta]) for a given log10(M) from Mark-Houwink parameters K and a."""
    if k_value <= 0:
        raise ValueError("K_value must be positive")
    return math.log10(k_value) + a_value * log_m


def compute_mh_log_eta_values(k_value: float, a_value: float, log_m_list: list[float] = (3.0, 6.0)) -> list[float]:
    """Computes log10([eta]) values for a list of log10(M) values."""
    return [compute_mh_log_eta_value(k_value, a_value, m) for m in log_m_list]


def validate_mark_houwink_entry(entry: dict) -> dict[str, bool]:
    """
    Validates numerical Mark-Houwink coefficients (a_value, K_value, and calculated log10([eta])).
    Returns a dict mapping error flag name -> boolean.
    """
    failed_flags = {
        "a_value_out_of_range": False,
        "K_value_out_of_range": False,
        "eta_out_of_range": False
    }

    # Check a_value range
    a_val = entry.get("a_value")
    if isinstance(a_val, str):
        try:
            a_val = float(a_val.strip())
        except ValueError:
            pass

    if isinstance(a_val, (int, float)):
        if not (MH_A_MIN <= a_val <= MH_A_MAX):
            failed_flags["a_value_out_of_range"] = True
    elif a_val is not None:
        failed_flags["a_value_out_of_range"] = True

    # Check K_value range
    k_val = entry.get("K_value")
    if isinstance(k_val, str):
        try:
            k_val = float(k_val.strip())
        except ValueError:
            pass

    if isinstance(k_val, (int, float)):
        if not (MH_K_MIN <= k_val <= MH_K_MAX):
            failed_flags["K_value_out_of_range"] = True
    elif k_val is not None:
        failed_flags["K_value_out_of_range"] = True

    # Check computed log10([eta]) values
    if isinstance(k_val, (int, float)) and isinstance(a_val, (int, float)) and k_val > 0:
        try:
            log_eta_vals = compute_mh_log_eta_values(k_val, a_val)
            for log_eta in log_eta_vals:
                if not (MH_LOG_ETA_MIN <= log_eta <= MH_LOG_ETA_MAX):
                    failed_flags["eta_out_of_range"] = True
                    break
        except Exception:
            pass

    return failed_flags
