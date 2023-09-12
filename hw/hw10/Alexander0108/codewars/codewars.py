#----------------------------------------------- Ball super ball -----------------------------------------

class Ball:

    def __init__(self, type = 'regular') -> None:
        self.type = type

    def ballType(self):
        return self.type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType())
print(ball2.ballType())

#----------------------------------------------- Color ghost ---------------------------------------------
import random

class Ghost:

    def __init__(self) -> None:
        pass

    @staticmethod
    def color():
        colors = ["white", "purple", "yellow", "red"]
        print (random.choice(colors))

ghost = Ghost()

ghost.color()

#----------------------------------------- Basic subclasses - Adam and Eve -------------------------------

class Human:

    def __init__(self, name) -> None:
        self.name = name

class Man(Human):

    def __init__(self, name) -> None:
        super().__init__(name)

class Woman(Human):

    def __init__(self, name) -> None:
        super().__init__(name)

def create():
    man = Man("Adam")
    woman = Woman("Eve")
    return [man, woman]

Adam_Eve = create()

for person in Adam_Eve:
    print("-----------")
    print(f"{person.name} is a member of the {person.__class__.__name__} class, a parental class for which this is {person.__class__.__base__.__name__}")

#-------------------------------------------- Classy Classes ---------------------------------------------

class Person:

    def __init__(self) -> None:
        pass

    def Constructor(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def getinfo(self):
        return f"{self._name} is {self._age} years old"


    def GetInfo(self):
        return f"{self._name} is {self._age} years old"
    
person1 = Person()
person1.Constructor("John", 34)
print(person1.getinfo)
print(person1.GetInfo())

#-------------------------------------------- Building Spheres -------------------------------------------

from math import pi

class Sphere:

    def __init__(self, radius: int, mass: int) -> None:
        self._radius = radius
        self._mass = mass
    
    def get_radius(self):
        print (self._radius)
    
    def get_mass(self):
        print (self._mass)

    def get_volume(self):
        self.volume = round(((4/3)*pi*self._radius), 5)
        print (self.volume)

    def get_surface_area(self):
        print (round((4*pi*self._radius**2), 5))

    def get_density(self):
        print(round((self._mass/self.volume), 5))

ball = Sphere(5, 10)

ball.get_radius()
ball.get_volume()
ball.get_surface_area()
ball.get_density()

#-------------------------------------------- Dynamic Classes --------------------------------------------

import re

def change_class_name(old_class, new_class_name):
    # Check if the new class name is valid
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_class_name):
        raise ValueError("Invalid class name. Class names must start with an uppercase letter and contain only alphanumeric characters.")

    # Create a new class with the desired name
    new_class = type(new_class_name, old_class.__bases__, dict(old_class.__dict__))

    # Delete the old class to avoid conflicts
    del globals()[old_class.__name__]

    return new_class

# Define a sample class
class OriginalClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")
        

# # Change the class name
# RenamedClass = change_class_name(OriginalClass, "RenamedClass") <--------- Checkout 

# Attempt to change the class name with an invalid name
try:
    InvalidClass = change_class_name(OriginalClass, "invalid-class")
except ValueError as e:
    print("Error:", e)