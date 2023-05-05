def isAlt(a):
    for i in range(1, len(a)):
        if (a[i-1]*a[i] > 0):
            return False
    return True


def isGrow(a):
    for i in range(1, len(a)):
        if (a[i-1] > a[i]):
            return False
    return True


def isMulti():
    for i in range(1, len(a)):
        d = a[i] / a[i-1]
        if (a[i-1] / a[i] != d):
            return False
    return True
    


def isAdd():
    for i in range(1, len(a)):
        d = a[i] - a[i-1]
        if (a[i-1] / a[i] != d):
            return False
    return True

n = int(input('Nhập số phần tử trong dãy số n = '))

aList = [0 for j in range(0, n)]

for i in range(0, n):
    aList[i] = int(input('list[' + str(i) + '] = '))
    
print('isAlt = ', isAlt(aList))
print('isGrow = ', isGrow(aList))
print('isMulti = ', isMulti(aList))
print('isAdd = ', isAdd(aList))