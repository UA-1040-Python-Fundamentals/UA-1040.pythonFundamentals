class Employees:
    quantity = 0
    lis = list()

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        self.__class__.quantity += 1
        self.lis.append(f'Name: {name}, Salary: {salary}')

    def number_employees(self):
        return f'Number of employees: {self.quantity}'

    def list_employees(self):
        return f'List of employees:\n {self.lis}'

    def info(self):
        return f'Employee information\nName: {self.name}\nSalary: {self.salary}'


def main():
    l1 = Employees('ff', 200)
    l2 = Employees('hh', 300)
    l3 = Employees('rr', 400)

    print(l1.list_employees())
    print(l2.info())
    print(l3.number_employees())
    print(Employees.__base__)
    print(Employees.__dict__)
    print(Employees.__name__)
    print(Employees.__module__)
    print(Employees.__doc__)


if __name__ == '__main__':
    main()
