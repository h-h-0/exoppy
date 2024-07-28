import numpy as np

def generate_light_curve(period, duration, depth, t_total, t_resolution=1000, noise_level=0.01):

    """

    Parameters:

        period      :   float 
                        orbital period of the exoplanet (in days)
        duration    :   float
                        duration of the planetary transit (in hours)
        depth       :   float
                        depth of the transit (fractional decrease in flux)
        t_total     :   float 
                        total duration of the observation (in days).
        t_resolution:   int
                        number of time points in the light curve.
        noise_level :   float 
                        level of Gaussian noise to add to the light curve.

    Returns:
        tuple       : Two arrays representing time and flux.
    
    """

    # time axis
    time = np.linspace(0, t_total, t_resolution)

    # phase of the transit, location of the exoplanet in front of the star
    phase = (time % period) / period

    # synthetic flux

    flux = np.ones_like(time)
    transit_duration = duration / 24.0  # convert from hours to days
    in_transit = np.abs(phase - 0.5) < transit_duration / 2.0 # checks if the exoplanet has reached in the middle or not
    flux[in_transit] -= depth

    # noise
    flux += np.random.normal(scale=noise_level, size=flux.shape)

    return time, flux
