class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}. Welcome!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "This is a static message."

person1 = Human("Alice")
person2 = Human("Bob")


print(person1.greet())
print(person2.greet())

print(Human.get_species())

print(Human.arbitrary_message())  #
