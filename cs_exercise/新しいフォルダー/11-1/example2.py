def mult_table():
    for i in range (1,10):
        row =''
        for s in range(1,10):
            res = s*i
            row += str(res) + "\t"
        print(row)


mult_table()