class Human:
    def __init__(self, name):
        self.name = name

    def display_welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "Hello to all other Homosapiens!"

person1 = Human("Даня")
person2 = Human("Ваня")
person3 = Human("Аня")

print(person1.display_welcome_message())
print(person2.display_welcome_message())
print(person3.display_welcome_message())

print(Human.species_info())
print(Human.arbitrary_message())
