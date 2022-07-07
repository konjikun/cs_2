def repeat(xs,n):
    list = []
    for s in xs:
        for i in range(n):
            list.append(s)
    return list

print(repeat(['I', 'have', 'a', 'pen'], 3))
print(repeat(['I', 'have', 'an', 'apple'], 0))