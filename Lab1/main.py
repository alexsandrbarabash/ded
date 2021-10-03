import matplotlib.pyplot as plt
import numpy as np

x0 = - 10 * np.pi / 2
x1 = 10 * np.pi / 2
step = .01

x = np.arange(x0, x1, step)

y = np.tan(x) / x
plt.plot(x, y)
plt.ylim(-5, 5)
plt.grid('grid', linestyle="-", color='black')
plt.show()