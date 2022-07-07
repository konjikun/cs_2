def stripe(w,h):
    for i in range(0,h//2):
        print('#' * w)
        print('+' * w)
    if h % 2 == 1:
        print('#' * w)

stripe(8,10)
