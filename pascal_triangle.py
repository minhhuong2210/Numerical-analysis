def factorial(n):
    f = 1
    while (n > 1):
        f = f * n
        n = n - 1
    return f
def ncr(n, r):
    return int(factorial(n) / (factorial(n-r) * factorial(r)))


n = 6
print("Ve tam giac Pascal: ")
for i in range(0, n+1):
    for j in range(0, i+1):
        print(ncr(i, j), end = " ")
    print("")