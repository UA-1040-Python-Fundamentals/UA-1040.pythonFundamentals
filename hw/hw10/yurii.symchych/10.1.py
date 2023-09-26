class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def get_area(self):
        length, width = self.sides[0], self.sides[1]
        return length * width

rectangle = Rectangle(675, 6666)
print(rectangle.get_perimeter())
print(rectangle.get_area())