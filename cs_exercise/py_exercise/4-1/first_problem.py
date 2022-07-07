import time
n = 1
s =[]
def endroll(lines):
    for s in lines:
        time.sleep(n)
        print(s)

endroll(['ini','unu'])