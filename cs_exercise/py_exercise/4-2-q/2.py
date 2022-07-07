def find(lst,x):
    for i in lst:
        if x == i:
            return True
    return False

print(find([1,2,3,4,5],9))