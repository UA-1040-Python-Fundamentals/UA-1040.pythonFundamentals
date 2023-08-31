import math

def s_rectangle() -> int:
    """
    The function receives two numerical values of the sides of the rectangle (a, b) and returns the area of the rectangle
    """
    a = int(input("Enter the value of side a: "))
    b = int(input("Enter the value of side b: "))
    s = a * b
    
    print(f"The area of a rectangle with sides {a} and {b} is: ", s)

def s_triangle() -> int:
    """
    The function receives three numerical values. The sides of the triangle (a, b) and the value of the angle between them (y). Returns the area of a triangle.
    """
    a = int(input("Enter the value of side a: "))
    b = int(input("Enter the value of side b: "))
    y = int(input("Enter the value of the angle between the sides y: "))
    s = 0.5 * a * b * math.sin(y)
    
    print(f"The area of a triangle with sides {a} and {b} and an angle {y} between them is:", s)


def s_circle() -> int:
    """
    The function receives a single numerical value of the radius of the circle (r). Returns the area of a circle.
    """

    r = int(input("Enter the radius value r: "))
    s = math.pi * (r ** 2)

    print(f"The area of a circle with radius {r} is:", s)


def end_menu():
    user_cont = input("Press 1 to continue or anything to finish: ")
    if user_cont != "1":
        return False