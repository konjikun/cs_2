class MenuItem:
    def __init__ (self, name, price, place):
        self.name = name
        self.price = price
        self.place = place
        return

    def show(self):
        print('{0} ({1}) @ {2}'.format(self.name, self.price, self.place))
        

mi = MenuItem("allen","1billion",1)
