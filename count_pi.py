from math import pi, fabs

def arctan(x):
    result = x - (x**3) / 3 + (x**5) / 5
    return result;
pi_count = 4 * (arctan(1/2) + arctan(1/3))
print('pi = %.6f' % pi_count)

pi_approx = fabs(pi - pi_count)
print('pi_approx = ', pi_approx)
print('pi_exact = ', pi_approx / fabs(pi_approx))