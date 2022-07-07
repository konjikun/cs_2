def num_to_str(n):
    exeption =['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    tenth_pl =['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    handreds_pl =['handred']
    h = n // 100
    n = (n - h * 100)

    t = n // 10  
    e = n % 10

#100の位
    if h > 0:
        h-1
        return exeption[h - 1] + ' ' + handreds_pl[0] + ' ' + 'and'+' ' + tenth_pl[(t - 2)] + ' ' + exeption[(e - 1)]

    elif n < 10:
        return exeption[e - 1] 

    elif n / 10:
        return tenth_pl[(t - 2)]   

    elif h == 0 :
        return tenth_pl[(t - 2)] +' ' + exeption[(e - 1)]
            
print(num_to_str(833)) 