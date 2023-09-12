class Human:
    def __init__(self, name):
        self.name = name

    def good_day(self):
        return f'Good day, {self.name}!'

    def species(self):
        return f'{self.name} is a member of the species Homosapiens'

    @staticmethod
    def message():
        return 'Have a nice day'
