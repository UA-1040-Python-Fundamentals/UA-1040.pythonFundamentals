class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides

    def inputSides(self):
        self.sides = [int(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print('The area of the rectangle is', area)

rectangle = Rectangle()

rectangle.inputSides()
rectangle.findArea()