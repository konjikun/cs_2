import random
def janken():
    enemy=10
    while enemy != 0 and enemy!=1 and enemy != 2:
        enemy = int(input('あなたは？ (0:グー、1:チョキ、2:パー) '))
    cp=random.randint(0,2)
    if cp == enemy:
        result2= 'あいこ'
    elif enemy == cp - 1 or (cp ==0 and enemy == 2):
        result2 = '勝ち'
    else:
        result2 = '負け'
    return str(result2)
print(janken())