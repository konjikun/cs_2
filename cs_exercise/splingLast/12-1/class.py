from unicodedata import name


class Person:
    def __init__(self,name,nationality,age):
        self.name = name
        self.nationality =nationality
        self.age = age
    
    def sayHello(self,name):
        print('こんにちは、{0}さん。私は{}です'.format(name,self.name))

#クラスの中の関数はメソッドと呼ぶ
    
imanishi = Person('今西', '日本','25')
print(imanishi.age)

    