import re
def check_zipcode(s):
    if re.fullmatch('[0-9]{3}-[0-9]{4}',s):
        return('OK')
    else:
        return('NG')

print(check_zipcode('116-0003'))