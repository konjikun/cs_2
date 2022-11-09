def selection_sort(lst):
    length = len(lst)
    cp=0
    sw=0
    for i in range(length):
        minpos=i
        for j in range(i + 1, length):
            cp+=1
            if lst[j] < lst[minpos]:
                minpos =j
        if i != minpos:
            sw+=1
            tmp = lst[i]
            lst[i] = lst[minpos]
            lst[minpos] = tmp
    return cp,' ',sw

print(selection_sort([3,5,2,1,4]))