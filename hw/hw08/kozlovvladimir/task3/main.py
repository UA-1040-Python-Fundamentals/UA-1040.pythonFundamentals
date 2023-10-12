from calculate import *

input_figure = int(input('''
1.Rectangle
2.Triangle
3.Circle:
'''))
if input_figure == 1:
    length= int(input("Enter length of rectangle:"))
    width= int(input("Enter width of rectangle:"))
    print(rectangle_calculate(length,width))
elif input_figure == 2:
    heigh = int(input("Enter heigh of triangle:"))
    base = int(input("Enter base of triangle:"))
    print(triangle_calculate(heigh,base))

elif input_figure == 3:
    radius = int(input("Enter radius of circle:"))
    print(circle_calculate(radius))
