def janken():
    import random
    win = 0
    lose =0
    drow =0
    for _ in range(5):
        enemy = int(input('あなたは？ (0:グー、1:チョキ、2:パー) '))
        cp=random.randint(0,2)
        if cp == enemy:
            drow += 1
            print('ドロー')
        elif enemy == cp - 1 or (cp ==0 and enemy == 2):
            win += 1
            print('勝ち')
        else:
            lose += 1
            print('負け')
    p = win/(win + lose)
    
    return '対戦結果 : 勝ち　' + str(win) + ' 負け　' + str(lose) + ' ドロー ' + str(drow) + ' 勝率 ' + str(p)
print(janken())