class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__([height, width])
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


r = Rectangle(5, 8)
print(f"The area of a rectangle is {r.area()} square centimetres.")
