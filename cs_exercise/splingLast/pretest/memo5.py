def s246(s):
    if ('2' in s or '4' in s or '6' in s):
        for i in s:
            if i!='2' and i !='4' and i != '6':
                return False
        return True
    else:
        return False

print(s246('446662624'))
print(s246(''))
print(s246('6646444'))
print(s246('6646428'))
ret = s246('8646422')
print(ret)

