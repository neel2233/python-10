import numpy as np
from numpy import sin, cos, arctan, sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace (-10, 10, 100)
y = np.linspace (-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
z = (xgrid - ygrid) ** 2

fig = plt.figure()
ax = fig.add_subplot(121, projection="3d")
ax1 = fig.add_subplot(122, projection="3d")

ax.plot_surface(xgrid, ygrid, z)
ax1.plot_surface(xgrid, ygrid, z)
ax1.set_zscale("log")
plt.show()
