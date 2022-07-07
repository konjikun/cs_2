def count_digit(line):

    result =0
    for i in line:
        if i.isdecimal() ==True:
            result += 1
    return result
    

   

print(count_digit('今日は5月10日'))