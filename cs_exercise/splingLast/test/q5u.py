def simplify(s):
    result =0
    restr =''
    aaa=0
    for j in s:
        result +=1
    
        if j =='!':
            aaa+=1
        else:
            if aaa > 0:
                restr+='!'
            aaa =0
            restr+=j
        if result ==len(s) and aaa >0:
            restr+='!'

    return restr

print(simplify('Sugeeeee!!! Wow!!!!'))
print(simplify('Hello! How are you?'))