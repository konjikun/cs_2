k = int(input('任意の整数を入力してください'))
s = 0
for i in range(1,k+1):
    re = 1 / (i**2)
    s += re
result =(6 * s) **0.5 
print(result)
