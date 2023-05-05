import numpy as np
import scipy as sp
from numpy import array, dot, vstack
from numpy.linalg import norm

A = array([(1,2,4), (1,3,9), (1,4,16)])
a1 = A[:, 0]
a2 = A[:, 1]
a3 = A[:, 2]

u1n = a1
u1 = u1n / norm(u1n)
r11 = norm(u1n)

u2n = a2 - np.dot(a2@u1.T, u1)
r12 = a2@u1.T
r22 = norm(u2n)
u2 = u2n / norm(u2n)

u3n = a3 - dot(a3@u1.T, u1) - dot(a3@u2.T, u2)
r13 = a3@u1.T
r23 = a3@u2.T
r33 = norm(u3n)
u3 = u3n / norm(u3n)

Q = vstack((u1, u2, u3)).T
print(Q)

R = array([(r11, r12, r13), (0, r22, r23), (0, 0 , r33)])
print("R = \n", R)

print("Sai so QR-A = \n", Q@R-A)