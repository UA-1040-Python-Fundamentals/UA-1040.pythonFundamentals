from math import pi


class Sphere(object):

    def __init__(self, r, m):
        self.r = r
        self.m = m

    def get_radius(self):
        return self.r

    def get_mass(self):
        return self.m

    def get_volume(self):
        return round((4 / 3 * pi * self.r ** 3), 5)

    def get_surface_area(self):
        return round((4 * pi * self.r ** 2), 5)

    def get_density(self):
        return round((self.m / (4 / 3 * pi * self.r ** 3)), 5)
