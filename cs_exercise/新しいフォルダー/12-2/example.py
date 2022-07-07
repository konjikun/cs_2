import math 
import re

while True:
    try:
        r = float(input('半径＝'))
        print(r *r*math.pi)
    except ValueError as error:
        print('エラー: ' + str(error))
        print('正しく数を入力してください')
