class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_info(self):
        print(f"Employee Name: {self.name}\nSalary: ${self.salary}")

# Test
employee1 = Employee("Anton", 30000)
employee2 = Employee("Liubomyr", 60000)

Employee.print_total_employees()

employee1.display_info()
employee2.display_info()

print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
print(Employee.__bases__)