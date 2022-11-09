def my_lcm(a,b):
    c=1
    d=1
    while a !=b:
        if a>b:
            b *=c
            c+=1
        else:
            a*=d
            d+=1
    return a
print(my_lcm(18,24))