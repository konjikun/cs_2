def gcd(a,b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    while True:
        r= a% b
        if r == 0:
            return b
        a = b
        b = r
print(gcd(33,15))