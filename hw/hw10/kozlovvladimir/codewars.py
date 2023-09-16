#1
class Ball:
    def __init__(self, ballType="regular"):
        self.ballType = ballType

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType)
print(ball2.ballType)

#2
from  random import choice
class Ghost:
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
print(ghost.color)

#3
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

#4
class Person :
    def __init__(self, age=0):
        self._age = age
        # using the getter method

    def get_age(self):
        return self._age
        # using the setter method

    def set_age(self, a):
        self._age = a

    age = property(get_age, set_age)

John = Person ()

# using the setter function
John.age = 34
print(John.age)

#5
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
