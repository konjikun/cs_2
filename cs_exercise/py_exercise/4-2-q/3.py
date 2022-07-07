def longest(ws):
    result =''
    for n in ws:
        if len(n) > len(result):
            result = n
    return result
                
print(longest(['ken','Sakamura','Bessho']))