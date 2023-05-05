x = [1970,1980,1990,2000]
y = [203.302, 226.542, 249.633, 281.428]
n = len(x)
t = 0

result = []


for k in range(n):
    for i in range(k,n):
        if (x[i] - x[k] != 0):
            t = (y[i] - y[k]) / (x[i] - x[k])
            y[i] = t
            print(t)
        