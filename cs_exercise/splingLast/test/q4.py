class Book :
    def __init__(self,title,year):
        self.title=title
        self.published=year

    def is_older_than(self,other):
        print(type(other))
        if self.published <=other:
            return True
        else:
            return False

gate = Book('Rashomon', 1915)
spider = Book('Kumo no ito', 1918)
hell = Book('Jigoku hen', 1918)

print(spider.title)
print(gate.published)
print(gate.is_older_than(spider))
print(spider.is_older_than(gate))
print(spider.is_older_than(hell))