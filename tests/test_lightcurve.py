import sys
import os
import pytest

# -------------------------------- #
#              path
# -------------------------------- #

module_dir = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'exoppy.py')))
sys.path.append(module_dir)


# -------------------------------- #
#         importing module
# -------------------------------- #

import exoppy.lightcurve as lc
import numpy as np


# -------------------------------- #
#              testing
# -------------------------------- #

def test_with_negative_depth():
    depth = -0.5
    with pytest.raises(ValueError, match="Transit depth must be in range 0 < depth < 1"):
        lc.with_depth(depth)

def test_with_undefined_depth():
    depth = 1.5
    with pytest.raises(ValueError, match="Transit depth must be in range 0 < depth < 1"):
        lc.with_depth(depth)
        
def test_with_radius_planet_smaller_than_star():
    R_planet = 1.0
    R_star = 1.0  # Same as planet, should raise error

    with pytest.raises(ValueError, match="The planet's radius must be smaller than the star's radius."):
        lc.with_radius(R_planet, R_star)

def test_with_radius_planet_larger_than_star():
    R_planet = 1.5
    R_star = 1.0  # Planet larger than star, should raise error

    with pytest.raises(ValueError, match="The planet's radius must be smaller than the star's radius."):
        lc.with_radius(R_planet, R_star) 

def test_with_radius_negative_radii():
    R_planet = -1.0  # Negative radius
    R_star = 1.0
    
    with pytest.raises(ValueError, match="Radii must be non-negative"):
        lc.with_radius(R_planet, R_star)

def test_with_noise_large_noise_level():
    period = 1.0
    duration = 2.0
    depth = 0.01
    t_total = 1.0
    t_resolution = 1000
    noise_level = 1.0  # Large noise level
    
    _, flux = lc.with_noise(period, duration, depth, t_total, t_resolution, noise_level)
    
    assert np.max(flux) > 1, "Maximum flux should exceed 1 due to high noise"
    assert np.min(flux) < 1 - depth, "Minimum flux should be less than 1 due to high noise"

def test_with_noise_short_observation():
    period = 1.0
    duration = 24.0  # 24 hours (1 day)
    depth = 0.01
    t_total = 0.5  # Observation less than one full transit
    t_resolution = 1000
    noise_level = 0.01
    
    time, flux = lc.with_noise(period, duration, depth, t_total, t_resolution, noise_level)
    
    assert len(time) == t_resolution, "Time array should have the correct resolution"
    assert len(flux) == t_resolution, "Flux array should have the correct resolution"

def test_with_radius_long_transit_duration():
    R_planet = 1.0
    R_star = 10.0
    transit_duration = 0.2  # Longer than time array
    num_points = 1000
    
    time, flux = lc.with_radius(R_planet, R_star, transit_duration, num_points)
    
    expected_depth = (R_planet / R_star) ** 2
    assert np.allclose(flux, 1 - expected_depth), "Flux should be constant with a long transit duration"
