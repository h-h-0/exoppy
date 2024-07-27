# Ideal_LCs

This python package is designed to generate synthetic datasets of exoplanet lightcurves with some given parameters of the host star and the exoplanet. When an exoplanet comes in between the observer and the host star, the flux emitted by the host star decreases. Due to this transit of exoplanet, an `U` shaped graph of flux vs time can be seen. This decrement in flux can be calculated using the transit depth or squared ratio quantity of the radius of host star and the radius of the exoplanet. 

$$ \text{Transit Depth}  \delta = \left( \frac{R_\text{planet}}{R_\text{star}} \right)^2 = \frac{\Delta F}{F} $$