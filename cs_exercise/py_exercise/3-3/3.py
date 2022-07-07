birth = int(input('生年月日（yyyymmdd）8桁を入力してください'))
if birth % 4 == 0:
    print('大吉！')
elif birth % 4 ==1:
    print('中吉！')
elif birth % 4 ==2:
    print('小吉')
else:
    print('凶')        