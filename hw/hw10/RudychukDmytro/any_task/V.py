# DESCRIPTION:
# Now that we have a Block let's move on to something slightly more complex: a Sphere
import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return print(self.radius)

    def get_mass(self):
        return print(self.mass)

    def get_volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return print(round(volume, 5))

    def get_surface_area(self):
        surface_area = 4 * math.pi *self.radius**2
        return round(surface_area, 5)
    
    def get_density(self):
        volume = (4/3) * math.pi * self.radius**3
        density = self.mass / volume
        return print(round(density, 5))

ball = Sphere(2, 50)
ball.get_radius()
ball.get_mass()      
ball.get_volume() 
ball.get_surface_area() 
ball.get_density()