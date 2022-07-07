def hit(a1,a2,a3,a4,b1,b2,b3,b4):
    hit_list = [a1,a2,a3,a4,b1,b2,b3,b4]
    hi = 0
    a = 0
    b = 0
    
    for i in range (4):
        if hit_list[0] == hit_list[4]:
            hi += 1
            hit_list.pop(0)

        else:
            a += 1
            b += 1
            hit_list.pop(0)
    return hi
print('(1234','4321)','=>',hit(1,2,3,4,1,4,3,2,),'hit')
