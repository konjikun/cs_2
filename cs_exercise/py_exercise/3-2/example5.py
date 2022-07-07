def filter_odd(ns):
    odd =[]
    for s in ns:
        if s % 2 ==1:
            odd.append(s)
    return odd                   
print(filter_odd([1,2,3,4,5,]))

#def filter_odd(ns):
#    odd =[]
   # for s in ns:
    #    if s % 2 ==1:
     #       for odd in s:
             #  return odd  ←これだと1でreturnされて一つしか無理,だから処理なしでも実行できる順番に入れるやつないのかな？                 
#print(filter_odd([1,2,3,4,5,]))