def take3(s):
    three =''
    n =0
    for i in range(3):
        three += s[n]
        n += 1
    return three
        


print(take3("INIAD"))
x = take3("Toyo University")
print(x)