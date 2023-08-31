class Employee:
    """
    This is the Employee class that represents employees with a name and salary.
    """
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

employee1 = Employee("Dania", 50000)
employee2 = Employee("Vania", 63000)
employee3 = Employee("Ania", 45000)

employee1.display_info()
employee2.display_info()
employee3.display_info()

Employee.display_total_employees()

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
