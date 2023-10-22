# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.

class Polygon:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__(a, b, 0, 0, 0, 0)
        self.area = a * b


test = Rectangle(5, 10)
print(test.area)