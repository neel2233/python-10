import numpy as np
from numpy import sin, pi
import matplotlib.pyplot as plt
import time

plt.ion()
a = 0
while (a / 6) < 1:
    b = 6
    x = [sin(a * t) for t in np.arange(0., 2 * pi, 0.01)]
    y = [sin(b * t) for t in np.arange(0., 2 * pi, 0.01)]
    plt.clf()
    plt.plot(x, y)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.03)
    a += 0.04