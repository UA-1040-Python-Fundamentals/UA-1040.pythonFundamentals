#Task 1

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides

    def input_sides(self):
        self.sides =[int(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)


    def get_square_of_rectangle(self):
        side_a, side_b = self.sides
        square_of_rectangle = side_b * side_a
        print(f'Square of the rectangle is {square_of_rectangle}')


rec = Rectangle()
rec.input_sides()
rec.get_square_of_rectangle()

print(Rectangle.mro())

#Task 2

class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Greetings {self.name}")

    @classmethod
    def classmethod(cls):
        return "This is a species of Homosapiens"

    @staticmethod
    def staticmethod():
        return "Arbitrary message"


person_a = Human("Aleks")
person_b = Human("Bohdan")


print(person_a.greet())
print(person_b.greet())

print(Human.classmethod())
print(Human.staticmethod())

#Task 3

class Employee:
    '''
     This is the Employee class that represents employees with  information about each of them individually.
    '''
    employee_counter = 0
    storage = {}
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        Employee.employee_counter += 1
        key, value = name, salary
        Employee.storage.update({key: value})


    @classmethod
    def employee_count(cls):
        return f"Found {cls.employee_counter} specialists"

    def all_employees(self, name):
        our = self.storage.get(name)
        return f"The salary of this worker is equal :\n {our}"

    def displays_information(self):
        return f'Employee information' \
               f'\nName: {self.name}' \
               f'\nSalary: {self.salary}'


employee_a = Employee('Suno', 50000)
employee_b = Employee("Kasta", 63000)

print(employee_a.displays_information())
print(employee_b.displays_information())
print(Employee.employee_count())
print(employee_a.all_employees('Suno'))

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")
