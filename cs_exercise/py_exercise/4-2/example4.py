def conseal(s):
    x =''
    for h in s:
        if h.isdecimal():
            h = '*'
        x += h
    return x
    
print(conseal('david securyty code 128046'))


