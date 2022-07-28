import re

def kkk(s):
    if re.fullmatch(r"\w+@\w+(\.\w+)*",s):
        print('e-mailアドレスです')
    else:
        print('notEmail')
    

kkk('d@s.k.k.k.k')
print("/k\.")