def abbrev (words):
    result =''
    for ini in words:
        result += ini[0]
    return(result)
print(abbrev(['Nippon','Housou','Kyoukai']))        