def check4(xs):
    result=0
    for i in xs :
        if i % 4==0:
            result+=0
        else:
            result+=1
    if result >0:
        return 'NG'
    else:
        return'OK'
    

ans = check4([4, 12, 16])
print(ans)
print(check4([12, 17, 40, 10]))
print(check4([8, 3, 12, 15]))
print(check4([8, 4]))
print(check4([5, 7, 11]))