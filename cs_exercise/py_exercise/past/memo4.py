def threedigits(nums):
    result =[]
    for i in nums:
        if i < 1000:
            if i >99:
                result.append(i)
    return result



print(threedigits([99, 100, 1000, 999]))
numbers = [1234, 567, 890, 1234, 12, 345]
print(numbers, "-->", threedigits(numbers))