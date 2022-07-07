def count_chars(s):
    result = {}
    for c in s:
        if c in result:
            result[c] +=1
        else:
            result[c] = 1
    return result

print(count_chars('iniad'))
