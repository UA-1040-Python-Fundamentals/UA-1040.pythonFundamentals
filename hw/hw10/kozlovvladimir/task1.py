class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        '''A quick, informational print statement.'''
        print(f'There are {self.number_of_sides} sides.')

class Rectangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  # list of two numbers

    def get_area(self):
        '''Return the area of the rectangle: length x width.'''
        x, y = self.lengths_of_sides
        return x * y

MyRectangle =Rectangle([3, 4, ])
print(MyRectangle.get_area())