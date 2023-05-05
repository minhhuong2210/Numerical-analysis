from math import factorial
result = 1
for i in range(1001):
    result += 1 / factorial(i)
    if (1 / factorial(i) <= (10**(-10)) ):
        print(i, 'true')
    else:
        print(i, 'false')
print('e = {0:.{1}}'. format(result, 10))