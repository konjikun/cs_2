import re 
while True:
    s = input("半径は？")
    if re.fullmatch('[0-9]*',s) :
        break
    print("入力に誤りがあります。もう一度入力してください。")
r = int(s)
print("面積＝", r * r * 3.14159)