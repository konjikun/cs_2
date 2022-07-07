num = 1
sum = 0
while True:
    marchandice = input(str(num) + '個目の商品の価格（円）を入力してください:')
    if marchandice == 'q':
        break
    num += 1
    sum += int(marchandice)

print('小計:',(sum))
tax = sum * 0.1

print('消費税(10%):', int(tax))
big_sum = sum + tax

print('計:',int(big_sum))