def my_min(numbers):
    x = numbers[0]
    for i in numbers:
        if i < x:
            x = i
    return x


print(my_min([90,30,22,79,60]))