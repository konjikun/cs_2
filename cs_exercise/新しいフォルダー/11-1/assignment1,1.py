def mikitani(yen):
    yen = str(yen)
    a= 0
    result =''
    yen =yen[len(yen)::-1]
    for i in yen:
        result += i
        if (len(yen) +a) - len(result) == 0:
            continue
        elif (len(result) - a) % 3 ==0:
            result += ','
            a +=1
    result = result[len(result)::-1]
    return result

print(mikitani(12345678912))