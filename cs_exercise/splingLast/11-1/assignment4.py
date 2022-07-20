import re
def us_to_bk(date):
    result = re.fullmatch('([0-9])[/]([0-9])[/]([0-9]{4})',date)
    return '{}/{}/{}'.format(result.group(2),result.group(1),result.group(3))
print(us_to_bk('9/4/2013'))