class Human:
    def __init__(self,name= None):
        self.name = name

    def greeting(self):
        return (f'Hello {self.name}')

    def homo_check(self):
        return (f'{self.name} is a Homosapiens')

    @staticmethod
    def message():
        return f'Have a nice day, Human!'


h = Human("Oleh")
print(h.greeting())
print(h.homo_check())
print(h.message())
