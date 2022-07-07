def hit(a,b):
    i = 0
    for _ in range(1,10):
        if a[i] == b[i]:
            i += 1
    return i
print("(1234, 4321) =>",hit([1,2,3,4],[4,3,2,1]),"hit")
print("(1234,1432) =>",hit([1,2,3,4],[1,4,3,2]),"hit")