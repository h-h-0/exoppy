import sys
import os

sys.path.append(os.path.dirname("E:\\Projects\\Ideal_LCs\\main.py"))

import exopy

data = exopy.with_noise(5, 10, 1, 10)

import matplotlib.pyplot as plt

data2 = exopy.with_radius(5, 20)
plt.plot(data[0], data[1])
plt.show()