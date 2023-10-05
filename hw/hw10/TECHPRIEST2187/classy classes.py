class Dude:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getter(self):
        print(self.name+"'s age is "+str(self.age))


chel = Dude("john",34)
chel.getter()