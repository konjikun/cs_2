class Person:
    def __init__(self, first, family, age):
        self.first_name = first
        self.family_name = family
        self.age = age

    def full_name(self):
        return self.first_name + ' ' + self.family_name

taro = Person('Taro', 'Toyo', 29)
hanako = Person('Hanako', 'Akabane', 25)

print(taro.first_name)
print(hanako.age)
print(taro.age)
taro.age = 45
print(taro.age)
print(taro.full_name())









