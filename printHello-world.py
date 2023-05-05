def calculate(A,x):
    A=str(A)
    x=float(x)
    
    listA=A.split()
    p=0
    
    for i in range(len(listA)):
        listA[i]=float[listA[i]]
        p+=listA[i]*(x**i)
    return p

print(calculate("1 2 3 4 5",0.5))