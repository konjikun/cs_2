temp = [29,28,27,27,31,32,33,28,27,33]

def summer_percentage(temp):
    per = 0
    sum = len(temp)
    for s in temp:
        if s >= 30:
            per += 1
    return (per / sum) * 100
        




print(summer_percentage(temp),'%')
