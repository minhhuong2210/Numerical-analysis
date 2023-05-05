import numpy as np
from scipy.interpolate import lagrange
from numpy import polyval

#thay noi suy da thuc y(x) = 3x^2 - 2x + 1
x = np.array([0, 1, 2])

f = lambda x: 3*x**2 - 2*x + 1
y = f(x)
P2 = lagrange(x, y)
print('Da thuc noi suy Lagrange la \n', P2)

z = np.array([3, 4])
P2z = polyval(P2, z)