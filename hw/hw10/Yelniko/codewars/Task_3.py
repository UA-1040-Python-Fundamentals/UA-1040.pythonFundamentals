class Human:
    pass


class Man(Human):
    def __init__(self, name):
        self.name = name


class Woman(Human):
    def __init__(self, name):
        self.name = name


def God():
    man = Man('Adam')
    women = Woman('Eve')
    return [man, women]
