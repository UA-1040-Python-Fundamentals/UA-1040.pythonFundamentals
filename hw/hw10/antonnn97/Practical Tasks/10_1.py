class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def area(self):
        if len(self.sides) == 2:
            return self.sides[0] * self.sides[1]
        else:
            return None

# Test
rectangle = Rectangle([4, 5])
print(rectangle.area())