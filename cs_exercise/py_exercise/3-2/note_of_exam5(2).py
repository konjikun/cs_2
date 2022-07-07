numbers = [1,2,3,4,5]
def append_zero(nums):
    #defの中に初めての関数ぶち込むと一番下のprintで定義されてないことになる！
    result = numbers
    result.append(0)
    return result
print (append_zero(result))
