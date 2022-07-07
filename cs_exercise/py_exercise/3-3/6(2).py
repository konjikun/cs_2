year = input('誕生年の西暦を入力してください:')
month = input('生まれ月を入力してください:')
day = input('誕生年の日付を入力してください')

if int(day) >32 or int(day) < 1 or int(month) < 1 or int(month) >13 or int(year) > 2022:
    print('エラー')
    exit()

lis =[int(year),int(month),int(day)]
s =[]
sum =0

for s in lis:
    sum += s

#素数かどうか判別
def prime_num(sums):
    for i in range(2,sums):
        if sums  % i == 0:
            return '素数でない'
    return '素数である'
    
if prime_num(sum) == '素数である':
    print('大吉！')
    exit()

x = 0

for i in range(4):
    x += 1
    sum +=1
    if prime_num(sum) == '素数である':
        break

if x == 1:
    print('中吉！')
elif x == 2:
    print('小吉！')
else:
    print('凶...')