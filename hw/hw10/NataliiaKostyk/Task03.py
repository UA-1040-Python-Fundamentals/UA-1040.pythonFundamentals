class Employee:
    """ Employee class represents an employee of a company.
    Properties:
    name = the name of the employee
    salary = the salary of the employee. """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def print_employee_count(cls):
        print(f"There are {cls.employee_count} employees.")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}$.")

    @staticmethod
    def display_class_info():
        print(f"Base classes: {Employee.__bases__}")
        print(f"Namespace: {Employee.__dict__}")
        print(f"Name: {Employee.__name__}")
        print(f"Module: {Employee.__module__}")
        print(f"Docstring: {Employee.__doc__}")


e1 = Employee("Natalia Green", 5000)
e2 = Employee("Bob Dylan", 6000)
e3 = Employee("Charlie Lockwood", 7000)

Employee.print_employee_count()
e1.display_info()
e2.display_info()
e3.display_info()
Employee.display_class_info()
