computer = 1850

computer1 =  computer// 1000
computer2 = (computer - computer1 * 1000) //100
computer3 = (computer - computer1 * 1000 - computer2 *100) //10
computer4 = (computer - computer1 * 1000) - (computer2 * 100) - (computer3 * 10) 

while True:
    you = (input('4桁の整数'))
    
    if you == '0':
        break

    if you.isdecimal() == False:
       print('四桁の整数で入力してください')
       continue

    you =int(you)
    you1 = you // 1000
    if you1 == 0 or you1 > 9:
       print('四桁の整数で入力してください')
       continue

#ここまでは正しく打ててるかの確認

    you1 =  you// 1000
    you2 = (you - you1 * 1000) //100
    you3 = (you - you1 * 1000 - you2 *100) //10
    you4 = (you - you1 * 1000) - (you2 * 100) - (you3 * 10) 


    hit =0
    
    if computer1 == you1:
        hit += 1
    if computer2 == you2:
        hit += 1
    if computer3 == you3:
        hit += 1
    if computer4 == you4:
        hit += 1

        #blowが複数出ない為にやる

    if you1 == you2 or you1 == you3 or you1 == you4:
        you1 = 10
    if you2 == you3 or you2 == you4:
        you2 = 11
    if you3 == you4:
        you3 = 12

    
    blow = 0
    if computer1 == you2 or computer ==you3 or computer == you4:
        blow +=1
    if computer2 == you1 or computer == you3 or computer == you4:
        blow +=1
    if computer3 == you2 or computer == you1 or computer == you4:
        blow +=1
    if computer4 == you2 or computer == you3 or computer == you1:
        blow +=1
    
    print('you:','',you)
    print(hit,' hit / ',blow,' blow')

    if hit == 4:
        break

    
