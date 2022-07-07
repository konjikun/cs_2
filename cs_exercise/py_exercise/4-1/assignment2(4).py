def sqrt(x):
    a = x
    for i in range(0,10):
        a = a -((a**2)-x) / (2*a) 
    return a
print(sqrt(3))