class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def get(self):
        print(f'Employee name: {self.name}, salary: {self.salary}')

    @classmethod
    def get_count(cls):
        print(f'Total emloyee’s: {cls.employee_count}')

Best_employee = Employee('i', 5000)
Maria = Employee('Maria', 5100)

Best_employee.get()
Maria.get()

Employee.get_count()
