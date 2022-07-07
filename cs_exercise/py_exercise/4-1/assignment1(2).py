def list_upper(xs):
    result = []
    for x in xs:
        x = x.upper()
        #result = result.append(x)でnoneになるのはなぜ？
        #答えは . の手前のみを編集する関数だから。破壊的メソッドで戻り値はnoneになる
        result.append(x)
    return result
print(list_upper('iniad'))
