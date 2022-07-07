def filtr_odd(xs):
    result =[]
    i = []
    for i in xs:
        if i %2 ==1:
            result.append(i)
    return result
print(filtr_odd(list(range(20))))