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
        return "Welcome, Homosapiens."