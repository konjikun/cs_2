# 一つ分の野菜をジュースにする関数を定義
def to_juice(vegetable):
   return vegetable + ' juice'

# ジュースにする野菜(と果物)のリスト
vegetables = ['apple', 'tomato', 'orange']

# vegetablesのすべての野菜をジュースにして表示
for s in vegetables :
  print(to_juice(s))