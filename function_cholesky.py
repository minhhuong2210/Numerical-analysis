from numpy import array
import numpy.linalg as la

A = array([[4,-2,4],[-2,5,-4],[4,-4,6]])
print(A)

L = la.cholesky(A)
print(L)