#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = 0.9 * np.random.rand(25)
y = 125 * np.random.rand(25)
s = 10 * np.random.rand(25)


plt.scatter(x, y, c='c', s=s, label="Data Points")
plt.xlabel("Height in Inches")
plt.ylabel("Weight in Pounds")
plt.show()