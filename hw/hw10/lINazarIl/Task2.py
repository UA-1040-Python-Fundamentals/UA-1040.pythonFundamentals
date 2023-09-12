class human():
    name = str()
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'Hello {self.name}')

    @classmethod
    def kind(cls):
        print('Homosapiens') if cls == human else print('Other entity')

    @staticmethod
    def arbitrary(self):
        print('Arbitrary message)')
        pass

some_person = human('some name')
some_person.say_hi()
human.kind()
human.arbitrary()
