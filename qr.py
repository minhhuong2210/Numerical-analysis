import numpy as np
from numpy.linalg import qr

x = np.array([[89,59,77], [59,107,59], [77,59,89]])
b = np.array([10], [2], [85])

n = 3
m = np.size(x)

vector_one = np.ones(np.size(x))
A = np.vstack((vector_one, x, x**2)).T

Q,R = qr(A)

print('Q = \n', Q)
print('R = \n', R)

