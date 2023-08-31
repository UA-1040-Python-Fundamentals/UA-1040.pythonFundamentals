
#-------------------------------------------------- Task 10.1 -------------------------------------------------
class polygon:

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def get_area(self):
        pass

class rectangle(polygon):

    def __init__(self, a_side, b_side, color) -> None:
        super().__init__("rectangle", color)
        self.a_side = a_side
        self.b_side = b_side

    def get_area(self):
        self.area = self.a_side * self.b_side
        return f"Area of the {self.color} {self.name}: {self.area}"

# For fun ........

class triangle(polygon):

    def __init__(self, a_side, b_side, c_side, color) -> None:
        super().__init__("triangle", color)
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def get_area(self):
        p = (self.a_side + self.b_side + self.c_side)/2
        if self.a_side + self.b_side <= self.c_side or self.a_side + self.c_side <= self.b_side or self.b_side + self.c_side <= self.a_side:
            return "Not a valid triangle"
        else:
            self.area = round((p*(p - self.a_side)*(p - self.b_side)*(p - self.c_side))**(1/2), 2)
            return f"Area of the {self.color} {self.name}: {self.area}"

class square(polygon):

    def __init__(self, a_side, color) -> None:
        super().__init__("square", color)
        self.a_side = a_side

    def get_area(self):
        self.area = self.a_side * self.a_side
        return f"Area of the {self.color} {self.name}: {self.area}"

a = rectangle(10, 20, 'red')
b1 = triangle(10,20,30, 'blue')
b2 = triangle(10,6,9, 'blue')
c = square(10, 'black')

print(a.get_area())
print(b1.get_area())
print(b2.get_area())
print(c.get_area())

input("Press any key to continune: ")
print("------------------------------------------------------------------------")
#-------------------------------------------------- Task 10.2 -------------------------------------------------

class Human:

    def __init__(self, name) -> None:
        self.name = name

    def greeting(self):
        return f"Greetings, {self.name}!"
    
    def species(self):
        return f"{self.name} is a member of the species Homosapiens"
    
    @staticmethod
    def message():
        return "Hello everyone!"
    
name = Human("Alex")

print(name.greeting())
print(name.species())
print(name.message())

input("Press any key to continune: ")
print("------------------------------------------------------------------------")
#-------------------------------------------------- Task 10.3 -------------------------------------------------

class Employees:

    '''This class is designed to populate a 
list with information about employees and retrieve 
information about each of them individually 
or all of them together at once'''

    number_of_employees = 0
    employees = []

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employees.number_of_employees += 1
        Employees.employees.append(f"Name: {self.name}, Salary: {self.salary}$")

    def NumberOfEmployees():
        return f"Number of employees: {Employees.number_of_employees}"

    def AllEmpInf():
        return f"Employees info: {Employees.employees}"
    
    def EmpInf(self):
        return f"Employee info: Name: {self.name}, Salary: {self.salary}$"
    
employer1 = Employees("Alex", 2000)
employer2 = Employees("Max", 1500)
employer3 = Employees("Jack", 3500)

print(employer1.EmpInf())
print(employer2.EmpInf())
print(employer3.EmpInf())
print(Employees.AllEmpInf())
print(Employees.NumberOfEmployees())

print(Employees.__base__)
print(Employees.__dict__)
print(Employees.__name__)
print(Employees.__module__)
print(Employees.__doc__)