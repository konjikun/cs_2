def num2str(xs):
    result =[]
    for i in xs:
        if i < 10:
            result.append(str(i))
        else:
            n = i //10
            n = n *10
            one = i - n
            n =str(n)
            one =str(one)
            s = n + '+' + one
            result.append(s)
    
    return result

print(num2str([10, 9, 22]))
xs = [1, 2, 10, 21]
print(num2str(xs))