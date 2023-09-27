# Taks 1
class Ball:
    def __init__(self, type="regular"):
        self.ball_type = type


# Task_2
import random


class Ghost:
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])


ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.color)
print(ghost2.color)


# Task_3
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# Task_4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

    def get_info(self):
        return self.info


# Task_5
from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        V = round(float(((4 / 3) * pi) *(self.radius ** 3)),5)
        return V

    def get_surface_area(self):
        S= round(float((4*pi)*(self.radius**2)),5)
        return S
    def get_density(self):
        p = round(float(self.mass/(((4 / 3) * pi) *(self.radius ** 3))),5)
        return p

# Task_6


def class_name_changer(cls, new_name) :
    if not new_name[0].isupper() or not new_name.isalnum():
        raise NameError('Invalid class name!')
    cls.__name__ = new_name