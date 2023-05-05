import numpy as np
import scipy.linalg as la

cond_A = la.expm_cond(A, np.inf)
print('Condition number of A is: ', cond_A)