def hyphen(s):
    result = ''
    for n in s:
        if n == '_':
            n = '-'
        result += n
    
    return result

print(hyphen('WELLB HUB_2 is next to HUB_1.'))
e = 'A little_used car is not a little used_car.'
print(hyphen(e))
