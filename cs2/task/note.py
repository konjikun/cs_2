def qsort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    lst1 = [x for x in lst if x < pivot]
    lst2 = [pivot]
    lst3 = [x for x in lst if x > pivot]

    return qsort(lst1) + lst2 + qsort(lst3)