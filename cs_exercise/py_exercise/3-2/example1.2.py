def month_to_str(m):
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    return months[m-1]
def date(m,d):
    return month_to_str(m) + ' ' + str(d)
print(date(3,15))      