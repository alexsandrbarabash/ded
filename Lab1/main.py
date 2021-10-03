import matplotlib.pyplot as plt
import numpy as np

x0 = float(input('Add x0:'))
x1 = float(input('Add x1:'))
step = float(input('Add step:'))


x = np.arange(x0, x1, step)

y = np.tan(x) / x
plt.plot(x, y)
plt.ylim(-5, 5)
plt.grid('grid', linestyle="-", color='black')
plt.show()