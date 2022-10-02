def e2a(s):
    result = ''
    for i in s:
        if i =='e':
            result+='a'
        else:
            result+=i
    return result


ans = e2a('exit')
print(ans)
print(e2a('destiny'))
print(e2a('eel'))
print(e2a('green'))
print(e2a('example'))