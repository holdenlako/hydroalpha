"""
hydroalpha: Computational Hydrotechnical Library
Author: Ing. Holden Lako
Affiliation: Faculty of Civil Engineering, Polytechnic University of Tirana (UPT)
ORCID: 0009-0009-3356-3612 | ISNI: 0000 0005 3183 3950
"""

from .core import (
    calculate_composite_alpha,
    apply_slope_correction,
    adjust_for_return_period
)
from .remote_sensing import (
    estimate_imperviousness_ndvi,
    calibrate_alpha_spectral
)

__version__ = "1.0.0"
__author__ = "Ing. Holden Lako"
__all__ = [
    "calculate_composite_alpha",
    "apply_slope_correction",
    "adjust_for_return_period",
    "estimate_imperviousness_ndvi",
    "calibrate_alpha_spectral",
]
