merchandise1 =int(input('１つ目の商品の金額を入力してください'))
merchandise2 = int(input('2つめの商品の金額を入力してください'))
subtotal = merchandise1 + merchandise2
print('小計は',subtotal)
tax =subtotal // 10
sum = tax + subtotal
print(tax)
print(sum)
