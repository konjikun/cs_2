password = 'fack' #現在のパスワード

while True:
    pwd = input('現在のパスワードを入力してください')
    if pwd != password:
        print('パスワードが違います')
        continue

    pwd1 = input('新しいパスワード')
    pwd2 = input('確認のためもう一度入力')
    if pwd1 != pwd2:
        print('同じパスワードを入力してください')
        continue
    else:
        break   #正しいパスワードが入力されたので無限ループ終了
password = pwd1    #パスワード更新する
print('パスワードが変更されました')

       
        