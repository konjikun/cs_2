def nearest(nums,x):

    for list in nums:
        n = nums[0]
        if abs(list - x) < abs(n - x):
            result = list
    return result

        
xs = [32, 8, 43, 90]
print(nearest(xs, 12))
n = nearest(xs, 38)
print(n)