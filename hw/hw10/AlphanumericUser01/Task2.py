# Create a class Human, everyone has a name
# create a method in the class that displays a welcome message to each person.
# Create a class method in the class that returns information that it is a species of "Homosapiens".
# And in the class create a static method that returns an arbitrary message

class Human:
    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        return f"""Greetings to {self.name}"""

    @classmethod
    def homosapiens(cls):
        return f"""It is a species of Homosapiens"""

    @staticmethod
    def random_msg():
        return "This is an arbitrary message"


a = Human("John Doe")
print(a.welcome_msg())
print(a.homosapiens())
print(a.random_msg())
