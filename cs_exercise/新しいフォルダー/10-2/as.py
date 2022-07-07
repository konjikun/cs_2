def repeat(xs,n):
    list = []
    for s in xs:
        list.append(s*n) 
    return list

print(repeat(['I', 'have', 'a', 'pen'], 3))
print(repeat(['I', 'have', 'an', 'apple'], 0))