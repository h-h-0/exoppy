# exoppy

[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE) [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-360/) [![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

This python package is designed to generate synthetic datasets of exoplanet lightcurves with some given parameters of the host star and the exoplanet. When an exoplanet comes in between the observer and the host star, the flux emitted by the host star decreases. Due to this transit of exoplanet, an `U` shaped graph of flux vs time can be seen. This decrement in flux can be calculated using the transit depth or squared ratio quantity of the radius of host star and the radius of the exoplanet. 

$$ \text{Transit Depth }  \delta = \left( \frac{R_\text{planet}}{R_\text{star}} \right)^2 = \frac{\Delta F}{F} $$

#### Dependencies 

- NumPy 

#### Acknowledgements 

Thanks to `Code/Astro` for arranging a workshop where we, K M Shariat Ullah, Hassan Habib and Anna Preis met for the first time. While learning about python packages, we had this idea to generate synthetic datasets for exoplanet lightcurves. It wouldn't be possible without the help of instructors and TA's of `Code/Astro`. 
