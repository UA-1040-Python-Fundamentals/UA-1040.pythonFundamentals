class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, I am {self.name}. Welcome!"

    @classmethod
    def species_info(cls):
        return "I am a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

person1 = Human("Марічка")
person2 = Human("Іван")

print(person1.welcome())
print(person2.welcome())
print(Human.species_info())
print(Human.arbitrary_message())