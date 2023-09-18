class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Загальна кількість працівників: {cls.total_employees}")

    def display_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

# Приклад використання:
employee1 = Employee("Олена", 50000)
employee2 = Employee("Петро", 60000)

employee1.display_info()
employee2.display_info()

Employee.display_total_employees()

# Відображення інформації про базовий клас та інші атрибути:
print(f"Базовий клас Employee: {Employee.__base__}")
print(f"Простір імен класу Employee: {Employee.__dict__}")
print(f"Назва класу Employee: {Employee.__name__}")
print(f"Назва модуля, у якому визначено клас Employee: {Employee.__module__}")
print(f"Панель документації класу Employee: {Employee.__doc__}")




