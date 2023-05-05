x = int(input())
result = x
for i in range(2,5):
    y = int(str(x)*i)
    result += y
print(result)