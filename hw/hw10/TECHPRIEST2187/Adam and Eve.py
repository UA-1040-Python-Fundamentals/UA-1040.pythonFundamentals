class Human:
    def __init__(self, ideology="not communist"):
        self.ideology = ideology


class Man(Human):
    def __init__(self, sex):
        super().__init__()
        self.sex = sex


class Woman(Human):
    def __init__(self, sex):
        super().__init__()
        self.sex = sex


hum = Human()
man = Man("male")
woman = Woman("female")
