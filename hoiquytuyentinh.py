import numpy as np
from numpy.linalg import solve, qr, norm


x = np.array([4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1])
b = np.array([102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72])

#x = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
#b = np.array([1.1506, 0.8671, 0.5596, 0.2927, 0])

n = 2
m = np.size(x)

vector_one = np.ones(np.size(x))
A = np.vstack((vector_one, x)).T

print('Ma tran A la \n ',A)

#Phuong phap phuong trinh chinh tac
c = solve(A.T@A, A.T@b)
print('c *', c)

#Nhu vay cthuc nghiem la y ~ f = lambda x: c[0] + c[1]@x + c[2]@x**2
y_approx = A@c

#Tinh toan do lech chuan
S = norm(y_approx - b)**2

print("Do lech chuan: ", np.sqrt(S/(m-n)))




