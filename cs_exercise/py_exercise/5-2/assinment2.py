# 山手線の駅の集合を定義(本当はもっとたくさん)
stations = {'shinjuku', 'akihabara', 'ueno', 'gotanda'}

while True:
  s = input('山手線の駅は? ')
  if s not in stations:
    print('ゲームオーバー')
    break

  # 1度使われた駅名は stations から削除
  stations.remove(s)
