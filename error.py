from math import fabs
a = 10.00
a_error = 0.05
b = 0.0356
b_error = 0.0002
c = 15300
c_error = 100
d = 62000
d_error = 500

S = a + b + c + d
Sapp = (a+a_error)+(b+b_error)+(c+c_error)+(d+d_error)
print(fabs(Sapp-S))
print(a_error+b_error+c_error+d_error)