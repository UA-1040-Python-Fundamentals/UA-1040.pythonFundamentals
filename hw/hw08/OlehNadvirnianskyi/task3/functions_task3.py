__all__ = ["rectangle","triangle","circle"]
from math import pi, pow
def rectangle(length, width):
    ''' Function calculates the area of a rectangle '''
    s_rectangle = int(length) * int(width)
    return s_rectangle
def triangle(heigh, base):
    ''' Function calculates the area of a triangle '''
    s_triangle = int(heigh)*int(base)/2
    return s_triangle
def circle(radius):
    ''' Function calculates the area of a circle '''
    s_circle = pi*(pow(int(radius),2))
    return s_circle