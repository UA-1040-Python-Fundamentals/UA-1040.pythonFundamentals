class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


class God:
    @staticmethod
    def creation():
        humans = None * 2
        humans[0] = Man("Adam")
        humans[1] = Woman("Eve")
        return humans
