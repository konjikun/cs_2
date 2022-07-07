def find_three(lst):
    result = 'none'
    for x in lst:
        if len(x) == 3:
            result = x
            break
    return result



print(find_three(['I', 'have', 'an','pen']))