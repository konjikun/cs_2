class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return abs((((self.x ** 2) + (self.y ** 2)) ** 0.5) - (((other.x ** 2) + (other.y ** 2))** 0.5))

