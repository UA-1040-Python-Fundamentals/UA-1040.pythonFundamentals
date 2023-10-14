class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, I am {self.name}. Welcome!"

    @classmethod
    def species_info(cls):
        return "I am a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "Hi, everybody!!!"

# Test
person = Human("Anton")
print(person.welcome_message())
print(Human.species_info())
print(Human.arbitrary_message())