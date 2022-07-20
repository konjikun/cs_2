import re
def count_uid(xs):
    lists =[]
    for i in xs:
        if re.match('s1f[0-9]{9}',i):
            result = i + '@iniad.org'
            lists.append(result)
    return len(lists)


in_s = ['INIAD','toyo','s1f102109999','s1f102008888','japan','s1f101907777','s1f101806666','iniad']
print(count_uid(in_s))