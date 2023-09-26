# I. Ball-super-ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")


# II. Color-ghost
import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]

        self.color = random.choice(colors)


# III. Basic-subclasses-Adam-and-Eve
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

# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# V. Building Spheres

import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

# VI. Dynamic Classes

def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name






