class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name} age is {self.age}"

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

# Test
john = Person("John", 34)
print(john.info)