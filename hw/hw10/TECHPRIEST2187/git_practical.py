# 1
class Polygon:
    def __init__(self, side1):
        self.side1 = side1


class Rect(Polygon):
    def __init__(self, side1, side2):
        super().__init__(side1)
        self.side2 = side2

    def square(self):
        return self.side1 * self.side2


# 2
class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hello " + self.name

    def species(self):
        return "I'm homosapience"

    @staticmethod
    def arbitrary():
        return "Hello, Hell"


# 3
class Employee:
    objcounter = 0

    def __init__(self, name, salary):
        Employee.objcounter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.objcounter -= 1

    def info(self):
        print("This is " + self.name + " his/her salary equals " + self.salary)

    def count(self):
        return Employee.objcounter


print(Employee.__base__, Employee.__dict__, Employee.__name__, Employee.__module__,Employee.__doc__)