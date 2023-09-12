class Polygon:
    def __int__(self, side_a, side_d):
        self.side_a = side_a
        self.side_d = side_d


class Rectangle(Polygon):

    def __init__(self):
        Polygon.__init__(self)
        self.area = 0

    def get_area(self):
        self.area = self.side_d * self.side_a
        return f'Area of the {self.area}'
