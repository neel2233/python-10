import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre

x = np.linspace(0, 1.3)
y1 = legendre(1)(x)
y2 = legendre(2)(x)
y3 = legendre(3)(x)
y4 = legendre(4)(x)
y5 = legendre(5)(x)
y6 = legendre(6)(x)
y7 = legendre(7)(x)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, y1, label="n = 1")
ax.plot(x, y2, label="n = 2")
ax.plot(x, y3, label="n = 3")
ax.plot(x, y4, label="n = 4")
ax.plot(x, y5, label="n = 5")
ax.plot(x, y6, label="n = 6")
ax.plot(x, y7, label="n = 7")
ax.legend()
ax.set_title("Полиномы Лежандра")
plt.show()
