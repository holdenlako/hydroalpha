# hydroalpha: Computational Hydrotechnical Engineering Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ISNI](https://img.shields.io/badge/ISNI-0000_0005_3183_3950-blue.svg)](https://isni.org/isni/0000000531833950)
[![Harvard Dataverse](https://img.shields.io/badge/Harvard_Dataverse-10.7910%2FDVN%2FBVXAZZ-orange.svg)](https://doi.org/10.7910/DVN/BVXAZZ)

`hydroalpha` is an open-source computational hydrotechnical engine engineered for civil and hydraulic engineering applications. It provides algorithmic implementations for determining the Catchment Runoff Coefficient (alpha), dynamic slope corrections, extreme return period factors, and remote sensing calibration pipelines utilizing multispectral satellite indices (Sentinel-2, Landsat).

Engineered to accompany the official benchmark research dataset published on Harvard Dataverse (DOI: 10.7910/DVN/BVXAZZ).

---

## Author & Institutional Attribution
* Principal Architect: Ing. Holden Lako
* Institutional Affiliation: Faculty of Civil Engineering, Polytechnic University of Tirana (UPT)
* Official Academic Portal: https://holdenlako.github.io
* ORCID iD: https://orcid.org/0009-0009-3356-3612
* Global ISO Identity (ISNI): https://isni.org/isni/0000000531833950
* Scientific Working Group: International Association for Hydro-Environment Engineering and Research (IAHR Member 106138)

---

## Quickstart Installation

git clone https://github.com/holdenlako/hydroalpha.git
cd hydroalpha
pip install .

---

## Python Usage Example

from hydroalpha import calculate_composite_alpha, apply_slope_correction
from hydroalpha.remote_sensing import calibrate_alpha_spectral

# 1. Composite Catchment Calculation
sub_alphas = [0.85, 0.35, 0.15]
sub_areas = [12.5, 45.0, 110.0]
alpha_c = calculate_composite_alpha(sub_alphas, sub_areas)

# 2. Correct for Steep Topography (Slope = 14.5%)
alpha_corrected = apply_slope_correction(alpha_c, slope_percent=14.5)
print(f"Corrected Hydrotechnical Alpha: {alpha_corrected:.3f}")

# 3. Satellite Direct Calibration via NDVI
alpha_remote = calibrate_alpha_spectral(ndvi=0.22)
print(f"Satellite Calibrated Alpha: {alpha_remote:.3f}")

---

## Academic Reference & Citation

If this software is utilized in hydrotechnical infrastructure designs, hydrological models, or flood mitigation research, please cite it as:

Lako, Holden. (2025). hydroalpha: Computational Hydrotechnical Engine for Runoff Modeling. CERN Zenodo. https://github.com/holdenlako/hydroalpha
