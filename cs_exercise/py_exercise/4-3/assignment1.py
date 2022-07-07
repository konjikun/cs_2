def sum_of_cubes(n):
    result = 0
    for i in range (1, n + 1):
        result += (i**3)
    return result

x =1

for i in range (1,11):
    print(sum_of_cubes(x))
    x += 1

