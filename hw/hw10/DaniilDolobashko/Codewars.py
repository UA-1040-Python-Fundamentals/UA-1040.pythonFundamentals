# 1
class Ball(object):
    def __init__(self, object = "regular"):
        self.ball_type = object

# 2
import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

# 3

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

# 4
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

# 5
import math

class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = 4 / 3 * math.pi * self.radius ** 3
        return round(volume, 5)
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)
    def get_density(self):
        density = self.mass / ((4/3) * math.pi * self.radius ** 3)
        return round(density, 5)

# 6
def class_name_changer(cls, new_name):
    if not new_name.isalnum():
        raise ValueError("New name must be alphanumeric")
    if not new_name[0].isupper():
        raise ValueError("New name must start with an uppercase letter")

    cls.__name__ = new_name