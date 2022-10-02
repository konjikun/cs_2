def simplify(s):
    result =0
    restr =''
    i = s[::-1]
    print(i)
    for j in range (len(s)):
        if i[j]!='!':
            break
        elif i[j]=='!':
            result+=1
    restr = s[:len(s)-result:1]
    if result > 0:
        restr += '!'
    return restr

print(simplify('Sugeeeee!!! Wow!!!!'))
print(simplify('Hello! How are you?'))