class Employee:
    """Employee Class Documentation"""

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        """Display information about the employee"""
        print(f"Name: {self.name}, Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        """Display the total number of employees"""
        print(f"Total Employees: {cls.total_employees}")

employee1 = Employee("John Doe", 50000)
employee2 = Employee("Alice Smith", 60000)

employee1.display_employee_info()
employee2.display_employee_info()

Employee.display_total_employees()

print(f"Base Classes: {Employee.__bases__}")
print(f"Class Namespace: {Employee.__dict__}")
print(f"Class Name: {Employee.__name__}")
print(f"Module Name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
