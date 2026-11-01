import numpy as np
from typing import Union, List

def calculate_composite_alpha(
    coefficients: Union[List[float], np.ndarray],
    areas: Union[List[float], np.ndarray]
) -> float:
    r"""
    Llogarit koeficientin e perbere te rrjedhjes (Weighted Runoff Coefficient)
    per nje pellg ujemmbledhes heterogjen.
    """
    c = np.asarray(coefficients, dtype=float)
    a = np.asarray(areas, dtype=float)
    
    if len(c) != len(a):
        raise ValueError("Vargjet e koeficienteve dhe siperfaqeve duhet te kene madhesi te njejte.")
    if np.any(c < 0.0) or np.any(c > 1.0):
        raise ValueError("Koeficienti i rrjedhjes duhet te jete brenda intervalit fizik [0.0, 1.0].")
    if np.any(a < 0.0) or np.sum(a) == 0.0:
        raise ValueError("Siperfaqet duhet te jene pozitive dhe shuma nuk mund te jete 0.")
        
    return float(np.sum(c * a) / np.sum(a))


def apply_slope_correction(
    base_alpha: float,
    slope_percent: float,
    method: str = "standard"
) -> float:
    r"""
    Aplikimi i korrigjimit te pjerresise se terrenit ne koeficientin e rrjedhjes.
    """
    if not (0.0 <= base_alpha <= 1.0):
        raise ValueError("Koeficienti baze duhet te jete ne intervalin [0.0, 1.0].")
        
    if method == "standard":
        if slope_percent < 2.0:
            cs = 0.95
        elif 2.0 <= slope_percent <= 7.0:
            cs = 1.00
        elif 7.0 < slope_percent <= 15.0:
            cs = 1.10
        else:
            cs = 1.20
        corrected_alpha = base_alpha * cs
        
    elif method == "chow":
        slope_rad = np.clip(slope_percent / 100.0, 0.001, 1.0)
        correction_factor = 1.0 + 0.15 * np.log10(slope_rad / 0.05)
        corrected_alpha = base_alpha * correction_factor
    else:
        raise NotImplementedError(f"Metoda {method} nuk njihet.")
        
    return float(np.clip(corrected_alpha, 0.05, 0.98))


def adjust_for_return_period(
    alpha: float,
    return_period_years: int
) -> float:
    r"""
    Korrigjimi i koeficientit per periudha te medha rikthimi (Permbytje ekstreme, Cf).
    """
    factors = {
        2: 0.85,
        5: 0.90,
        10: 1.00,
        25: 1.10,
        50: 1.20,
        100: 1.25
    }
    closest_t = min(factors.keys(), key=lambda k: abs(k - return_period_years))
    cf = factors[closest_t]
    
    return float(np.clip(alpha * cf, 0.05, 0.99))
