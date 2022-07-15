def laugh(s):
    result = 0
    restr =''    
    i = s[::-1]
    for j in range (len(s)):
        if i[j] != 'w':
            break
        elif i[j] =='w':
            result+=1
    restr = s[:len(s)-result:1]
    if result > 0:
        restr += '笑'

    return restr

print(laugh('wすげぇwww'))