def repeat(s,n):
    result =''
    for i in s:
        result += i * n
    return result


print(repeat("INIAD", 3))
x = repeat("Toyo", 2)
print(x)