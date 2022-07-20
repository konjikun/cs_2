import re
def exists21(xs):
    for i in xs:
        if re.match('s1f[0-9]{2}21[0-9]{5}',i):
            return True
        else:
            return False

in_s = ['INIAD','toyo','s1f102109999','s1f102008888','japan','s1f101907777','s1f101806666','iniad']
print(exists21(in_s))