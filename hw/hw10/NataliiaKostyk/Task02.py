class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to this chat.")

    @classmethod
    def get_species(cls):
        return "We are Homosapiens, the most intelligent species on the Earth."

    @staticmethod
    def say_smth():
        return "This is a static method which can be called without an instance."


h1 = Human("Alice")
h1.greet()
print(Human.get_species())
print(Human.say_smth())

h2 = Human("Bob")
h2.greet()
print(h2.get_species())
print(h2.say_smth())
