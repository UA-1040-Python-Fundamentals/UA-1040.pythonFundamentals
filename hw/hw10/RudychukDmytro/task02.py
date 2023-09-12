class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}")

    def inform(self):
        print("This species is homosapiens")

    @staticmethod
    def message():
        print("Message of staticmethod")


human1 = Human("Oleg")
human2 = Human("Anna")

human1.hello()
human2.hello()

human1.inform()
human2.inform()

Human.message()