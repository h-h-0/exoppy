import numpy as np

def with_noise(period, duration, depth, t_total, t_resolution=1000, noise_level=0.01):

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


def with_radius(R_planet, R_star, transit_duration=0.01, num_points=1000):

    """

    Parameters:

        R_planet (float)        : Radius of the planet in Jupiter radii.
        R_star (float)          : Radius of the star in Solar radii.
        transit_duration (float): Duration of the transit in days.
        num_points (int)        : Number of data points in the lightcurve.

    Returns:

        tuple       : Two arrays representing time and flux.

    """
    
    # Calculate the transit depth
    delta = (R_planet / R_star) ** 2

    # Create a time array
    time = np.linspace(-0.05, 0.05, num_points)

    # Create a flux array
    flux = np.ones_like(time)

    # Define the transit duration and depth
    in_transit = np.abs(time) < (transit_duration / 2)
    flux[in_transit] -= delta

    return time, flux
