class Employee:
    """
    Each employee has characteristics such as name and salary.
    """
    number_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1

    @classmethod
    def number_of(cls):
        print(f"Total Employees: {cls.number_of_employees}")

    def name_and_salary(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")



employee1 = Employee("Donald Duck", 100)
employee2 = Employee("Mickey Mouse", 200)
employee3 = Employee("Barbie", 300)

employee1.name_and_salary()
employee2.name_and_salary()
employee3.name_and_salary()

Employee.number_of()

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
