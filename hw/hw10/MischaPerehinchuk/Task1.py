class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print(f"Периметр прямокутника: {rectangle.perimeter()}")
print(f"Площа прямокутника: {rectangle.area()}")
