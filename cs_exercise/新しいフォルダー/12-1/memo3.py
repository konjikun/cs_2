class MenuItem:
    def __init__(self, name, price, place):
        self.name = name
        self.price = price
        self.place = place
        
menu =[
    MenuItem("鮭フライタルタルソース", 420, "WELLB"),
    MenuItem("照りマヨチキンセット", 500, "WELLB"),
    MenuItem("油淋鶏丼セット", 390, "INIAD"),
    MenuItem("マンゴープリン", 280, "INIAD"),
    MenuItem("醤油ラーメン", 300, "WELLB"),
]

for item in menu:
    print('{0} ({1}) @ {2}'.format(item.name, item.price, item.place))