import sys
import os

# Get the absolute path of the directory containing exopy.py
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'exopy.py'))
module_dir = os.path.dirname(module_path)

# append the directory to sys.path
sys.path.append(module_dir)

# importing the module 
import exopy.lightcurve as lightcurve

test1 = lightcurve.with_noise(5, 10, 1, 10)
test2 = lightcurve.with_radius(5, 20)


# visualizing the functions
import matplotlib.pyplot as plt
plt.plot(test2[0], test2[1])
plt.show()
