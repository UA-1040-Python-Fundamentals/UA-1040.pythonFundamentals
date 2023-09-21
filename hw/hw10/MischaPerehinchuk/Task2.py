class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привіт, якщо мене звуть {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "Допобачення"


person = Human("Іван")
person.greet()
print(f"Це вид: {person.species()}")
print(f"Випадкове повідомлення: {Human.random_message()}")
