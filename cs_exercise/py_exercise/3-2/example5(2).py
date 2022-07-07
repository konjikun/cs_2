numbers = [1,2,3,4,5]
#もしくは5行目
result = numbers.copy()
def append_zero(nums):
    #result = nums.copy()
    result.append(0)
    return result
print(append_zero(result))
print(numbers)    
