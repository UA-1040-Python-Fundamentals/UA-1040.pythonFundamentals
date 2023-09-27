class Employers:
    '''
    This class is created to operate with information about employers.
    '''
    employers = []
    num_empl = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employers.num_empl += 1
        Employers.employers.append(f"Name:{self.name},\n Salary:{self.salary}$\n")

    def info_empl():
        return f'Employers info: {Employers.employers}'

    def dicribe_employeer(self):
        return f"Info about employer:\nName:{self.name} \nSalary:{self.salary}$\n"

    def number_of_empl():
        return f"Amount of employers is {Employers.num_empl}\n"


empl_1 = Employers("Alex", 2034)
empl_2 = Employers("Oleh", 5030)
empl_3 = Employers("Victor", 1504)
empl_4 = Employers("Alyona", 3500)
print(empl_1.dicribe_employeer())
print(empl_2.dicribe_employeer())
print(empl_3.dicribe_employeer())
print(empl_4.dicribe_employeer())

print(Employers.info_empl())
print(Employers.number_of_empl())

print(Employers.__base__)
print(Employers.__dict__)
print(Employers.__name__)
print(Employers.__module__)
print(Employers.__doc__)
