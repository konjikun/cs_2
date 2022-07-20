import re
def time_diff(t1,t2):
    t3 = t1+','+t2
    time = re.search('([0-9]+):([0-9]+),([0-9]+):([0-9]+)',t3)
 
    a =int(time.group(1)) - int(time.group(3))
    if a != 0 and a < 0:
        a +=1
    elif a!=0 and a >=0:
        a-=1
    b =60 - abs((int(time.group(2)) - int(time.group(4))))
    
    return abs(a)*60 + abs(b)
print(time_diff('23:15','2:50'))