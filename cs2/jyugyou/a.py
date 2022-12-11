import random

def append_hundred(lst):
    for _ in range(100):
        value = random.randint(1,100)
        lst.append(value)

for i in range(1, 6):
    temp_lst = [0] * i *1000
    %timeit append_hundred(temp_lst)