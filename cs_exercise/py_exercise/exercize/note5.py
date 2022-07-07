def auth(p):#pはもともと設定されているパスワード
    for i in range(3):
        pwd = input('パスを入力')#パスワード確認し商品購入
        if pwd == p:
            #lenで文字列を数字で返す
            return len(p)
    return False
print(auth('app'))