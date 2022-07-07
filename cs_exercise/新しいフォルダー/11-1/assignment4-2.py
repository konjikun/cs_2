import re
def time_diff(t1,t2):
    t3 = t1+','+t2
    time = re.search('([0-9]+):([0-9]+),([0-9]+):([0-9]+)',t3)
 
    a =int(time.group(1)) - int(time.group(3))
    b =int(time.group(2)) - int(time.group(4))
    if abs(b) >30:
        if int(time.group(1))> int(time.group(3)):
            b = int(time.group(1)) + (60 - int(time.group(3)))
        elif int(time.group(1)) == int(time.group(3)):
            return abs(b)
        else:
            b = int(time.group(3)) + (60-int(time.group(1)))
        if a <0:
            a+=1
        else:
            a-=1
    return abs(a)*60 + abs(b)
print(time_diff('23:15','2:50'))