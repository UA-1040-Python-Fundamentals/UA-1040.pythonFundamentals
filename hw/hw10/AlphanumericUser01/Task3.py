# Create an employee class. Each employee has characteristics such as name and salary
# The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees
# and a method that displays information about each employee in particular, namely the name and salary
## In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__),
## the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee:
    """Employee Class that show employees and their salaries"""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def employee_total(cls):
        print(f"""Total Employees are: {Employee.counter}""")

    def employee_attributes(self):
        print(f"""Employee name is: {self.name}""")
        print(f"""Employee salary is: {self.salary} UAH""")


a = Employee("John Doe", 1000000)
b = Employee("Jane Dou", 30555)
c = Employee("James Doe", 50555)

a.employee_attributes()
b.employee_attributes()
Employee.employee_total()

print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
