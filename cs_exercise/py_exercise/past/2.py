def get_x(a,b,c):

    y1 = c
    x = (y1 - b) / a
    y = a * x + b
            
    return x


print(get_x(2,1,0))
x = get_x(-2,3,-2)
print(x)