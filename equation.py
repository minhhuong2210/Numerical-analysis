from math import sqrt, fabs
def sol(a, b, c):
    denta = b*b - 4*a*c;
    if (denta < 0):
        print('No solution');
    if (denta == 0):
        x = -b/(2*a)
        print('x = ', x);
    if (denta > 0):
        x1 = float((-b+sqrt(denta))/(2*a))
        x2 = float((-b-sqrt(denta))/(2*a))
        if (fabs(fabs(b) - sqrt(denta)) < 10**(-4)):
            if (b > 0):
                x1 = (-2 * c)/(b + sqrt(denta))
            else:
                x2 = (-2 * c)/(b - sqrt(denta))
        print('x1 = ', x1, 'x2 = ', x2);
a = 1
b = -((1e+9) + (1e-9))
c = 1
print('a = ', a, 'b = ', b, 'c = ', c)
sol(a, b, c)

a = 1
b = -((1e+6) + (1e-6))
c = 1e-6
print('a = ', a, 'b = ', b, 'c = ', c)
sol(a, b, c)