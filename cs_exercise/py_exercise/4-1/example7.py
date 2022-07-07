#結構使うから解答例もしっかり確認！
def abbrev(s):
    s_len = len(s)
    result =''
    for i in range(0,s_len):
        if i % 2 ==0:
            result += s[i]
    return result

print(abbrev('kuwasiku'))