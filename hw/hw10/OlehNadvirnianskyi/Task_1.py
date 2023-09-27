class Polygon:
    def __init__(self, num):
        self.n = num
        self.sides = [0 for i in range(num)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}:")) for i in range(self.n)]

    def showSides(self):
        for i in range(self.n):
            print(f"Side{i + 1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def AreaRect(self):
        a, b = self.sides
        s = a * b
        print(f'The area of rectangle is {s} cm2')


t = Rectangle()

t.inputSides()

t.showSides()

t.AreaRect()