class person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def hi(self):
        print('hi ?' , 'I am' , self.name)

numbers = [1,2,3,]
names = ['a','b','c']
p = person('bold', 22)
print(p.name)
p.hi()
p2 = person('baatar', 66)
print(p2.name)
p2.hi()