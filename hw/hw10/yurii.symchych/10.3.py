class Employee:
    # Class attribute to keep track of the total number of employees
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Increment the total number of employees when a new employee is created
        Employee.total_employees += 1

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def total_employee_count(cls):
        return f"Total employees: {cls.total_employees}"

employee1 = Employee("Марічка", 100000)
employee2 = Employee("Іван", 90000)

print(employee1.display_info())
print(employee2.display_info())
print(Employee.total_employee_count())


print(Employee.__bases__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)