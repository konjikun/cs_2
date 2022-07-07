def count_chars(s):
    result = {}
    for c in s:
        if result[c] in s:
            result +=1
        else:
            result[c] = 1
    return result

print(count_chars('iniad'))

#4行目でkey error i がでる。iはどっからわいた？