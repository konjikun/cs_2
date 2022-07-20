def count(s):
    result =0
    for i in s:
        if i == 'e':
            result +=1
    return result

print(count('enemies enter from east'))