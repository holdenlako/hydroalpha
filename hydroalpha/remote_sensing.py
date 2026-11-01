import numpy as np
from typing import Union

def estimate_imperviousness_ndvi(
    ndvi: Union[float, np.ndarray],
    ndvi_veg: float = 0.70,
    ndvi_soil: float = 0.15
) -> Union[float, np.ndarray]:
    r"""
    Llogarit fraksionin e siperfaqes se papershkueshme (Impervious Fraction)
    bazuar ne indeksin spektral NDVI te sateliteve Sentinel-2 / Landsat.
    """
    ndvi_arr = np.asarray(ndvi, dtype=float)
    fractional_veg = (ndvi_arr - ndvi_soil) / (ndvi_veg - ndvi_soil)
    fractional_veg = np.clip(fractional_veg, 0.0, 1.0)
    
    impervious_fraction = 1.0 - np.power(fractional_veg, 1.5)
    return float(impervious_fraction) if ndvi_arr.ndim == 0 else impervious_fraction


def calibrate_alpha_spectral(
    ndvi: Union[float, np.ndarray],
    alpha_impervious: float = 0.90,
    alpha_pervious: float = 0.25
) -> Union[float, np.ndarray]:
    r"""
    Kalibron koeficientin e rrjedhjes nga te dhenat spektrale satelitore.
    """
    imp_frac = estimate_imperviousness_ndvi(ndvi)
    alpha = imp_frac * alpha_impervious + (1.0 - imp_frac) * alpha_pervious
    return np.clip(alpha, 0.05, 0.98)
