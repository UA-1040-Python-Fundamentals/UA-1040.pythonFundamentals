class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    rectangle = Rectangle(int(input()), int(input()))
    print(f"Area of the rectangle: {rectangle.area()} square units")