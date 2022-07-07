def hello(name):
    """引数 name で指定された人へのあいさつ文を返す
    プログラム"""
    return "Hello,{0}san!".format(name)
help(hello)
hello("Enryo")