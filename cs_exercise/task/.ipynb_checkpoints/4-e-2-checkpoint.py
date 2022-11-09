def simple_qsort(lst):
    global n
    n += 1
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    lst1 = [x for x in lst if x < pivot]
    lst2 = [x for x in lst if x == pivot]
    lst3 = [x for x in lst if x > pivot]
    print(lst2)
    print(lst1)
    print(lst3)
    return simple_qsort(lst1) + lst2 + simple_qsort(lst3)

n=0
print(simple_qsort([0,0,0,0,0,0,0,0,0,0]))
print(n)