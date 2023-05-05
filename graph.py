from numpy import  polyval
import matplotlib.pyplot as plt

import numpy as np

p = [7.85714285, -11.64571429, 5.17]

xp = np.linspace(0.2, 0.5, 100)
plt.plot(x, y, 'rs', xp, polyval(p, xp), '-')
plt.grid(1)
plt.show()