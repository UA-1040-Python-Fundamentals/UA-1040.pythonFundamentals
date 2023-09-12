class Employee:
    """
    Employee class represents an employee in a company.

    Attributes:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
    """
    
    total_employee = 0

    def __init__(self, name, salary) -> None:
        """ 
        the initialization of the class object and the increment of the counter during initialization
        """
        self.name = name
        self.salary = salary
        Employee.total_employee += 1

    def __del__(self) -> None:
        """
        reduction of the employee counter when the class object is deleted
        """
        Employee.total_employee -= 1

    @staticmethod
    def total_information() -> str:
        """
        the method outputs general information about the number of employees
        """

        print(f"Total employee: {Employee.total_employee}")
    
    def employee_info(self) -> str:
        """
        method outputs information about the employee (name and salary)
        """

        print(f"Name: {self.name}, salary: {self.salary} $")

employee1 = Employee("Ivan Ivanov", 800)
employee2 = Employee("Ruslan Komar", 1200)
employee3 = Employee("Anna Ivanrnenko", 900)
employee4 = Employee("Svitlana Onushuk", 1000)

employee1.employee_info()
employee2.employee_info()


Employee.total_information()

employee2.__del__()

Employee.total_information()


print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation string: {Employee.__doc__}")
    

    

    
