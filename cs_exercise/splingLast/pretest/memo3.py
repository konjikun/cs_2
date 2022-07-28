def calc70(xs):
    result=0
    for a in xs:
        if a >70 and a%2==0:
            result+=1

    return result

ans = calc70([35, 160, 200, 20])
print(ans)
print(calc70([35, 165, 200, 20]))
print(calc70([120, 50, 40, 10]))
print(calc70([140, 76, 12, 155]))
print(calc70([100, 100, 70, 20]))    
