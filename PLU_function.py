import numpy as np
import scipy.linalg as la

A = np.array([[2, 4, 8], [10, 12, 0], [0, 2, 8]])
print('A = ', A)

In = np.eye(3)
print(In)

A1 = np.hstack((A, In))
print('A1 is: \n', A1)

P, L, U = la.lu(A1)
print('U is: \n', U)

X = la.solve(U[:,0:3],U[:,3:6])
invA = X
print('X is: \n', X)