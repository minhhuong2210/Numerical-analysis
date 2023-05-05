import numpy as np

def gauss(A, b):
    c = 0
    while (c < len(A) - 1):
        for i in range(c+1, len(A)):
            h = float(A[i][c] / A[c][c])
            b[i] = b[i] - h * b[c]
            for k in range(c, len(A)):
                A[i][k] = float(A[i][k] - h * A[c][k])
                L[i][c] = h
        c += 1
    print("L:", L)
    print("U:", A)
    print("b:", b)
A = np.array([[]])