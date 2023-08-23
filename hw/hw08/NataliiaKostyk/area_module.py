from math import pi, pow


def rectangle_area(a, b):
    """This function calculates the area of a rectangle"""
    return round(a * b, 2)


def triangle_area(h, a):
    """This function calculates the area of a triangle"""
    return round(0.5 * h * a, 2)


def circle_area(r):
    """This function calculates the area of a circle"""
    return round(pi * pow(r, 2), 2)
