# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.radius = int(radius) if isinstance(radius, int) else float(radius)
        self.mass = int(mass) if isinstance(mass, int) else float(mass)
        self.volume = 4 / 3 * pi * radius ** 3

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(self.volume, 5)

    def get_surface_area(self):
        surface_area = 4 * pi * self.radius ** 2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.volume
        return round(density, 5)


import codewars_test as test
# from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        ball = Sphere(2,50)

        test.assert_approx_equals(ball.get_radius(),2, margin=1e-5, message="Check radius")
        test.assert_approx_equals(ball.get_mass(),50, margin=1e-5, message="Check mass")
        test.assert_approx_equals(ball.get_volume(), 33.51032, margin=1e-5, message="Check volume")
        test.assert_approx_equals(ball.get_surface_area(),50.26548, margin=1e-5, message="Check area")
        test.assert_approx_equals(ball.get_density(),1.49208, margin=1e-5, message="Check density")