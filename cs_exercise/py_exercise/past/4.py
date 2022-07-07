def hi_val(nums):
    result =[]

    for i in nums:
        if i > 90:
            result.append(i)
    return result


xs = [30, 80, 40, 90]
print(xs, "-->", hi_val(xs))
ys = [100, 90, 89, 91, 100]
print(ys, "-->", hi_val(ys))