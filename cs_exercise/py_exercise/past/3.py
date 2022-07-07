def num_sign(x):
    if x > 0:
        return 'plus'
    
    elif x == 0:
        return 'none'
    
    else:
        return 'minus'

print(num_sign(10))
print(num_sign(0))
print(num_sign(-2))