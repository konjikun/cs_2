from email.errors import ObsoleteHeaderDefect
from tkinter import W


class BodyShape:
    def __init__(self,h,w):
        self.height = h
        self.weight = w
    
    def is_taller_than (self,other):
        if self.height >= other.height:
            return False
        else:
            return True

taro = BodyShape(170.0, 60.0)
hanako = BodyShape(160.0, 50.0)
print(hanako.height)
160.0
print(taro.is_taller_than(hanako))