class polygon:
    def __init__(self, vertices):
        self.vertices_num = vertices

class rectangle(polygon):
    def __init__(self, a, b):
        super().__init__(4)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

print('Please enter sizes of rectangle sides: ')
rect = rectangle(int(input('A side: ')), int(input('B side: ')))
print('Area of rectangle: ', rect.area())