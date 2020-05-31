class person:
    fname = 'bbold'
    lname = 'timb'

    def hi(self):
        print('Hi i am', self.fname)

p1 = person()
p2 =  person()
print(p1.fname)
p1.hi()
print(p2.lname)
p2.hi()