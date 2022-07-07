# randomモジュールを読み込む
import random

# 献立の候補一覧
meals = ["カレー", "ラーメン", "焼肉定食"]

for m in range(1, 31):
  # mealsの中からランダムに1つだけ選択
  item = random.choice(meals)

  print("4月", m, "日の献立は", item, "にしましょう")