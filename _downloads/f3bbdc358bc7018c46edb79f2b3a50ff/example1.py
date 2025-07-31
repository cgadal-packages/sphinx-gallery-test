"""
============
Example 1
============

Test

"""

import numpy as np

from mytoolbox.module1 import my_plot

x, y = np.random.random((100,)), np.random.random((100,))

my_plot(x, y)
