# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.
# (To perform the task, you need to import the math module, and from it the
# pow() function and the value of the variable pi, and module, which contains
# three functions for finding areas, into the main program. The basic logic of the
# program is executed in the main module).

from math import pow, pi


def area_calculation():
    while True:
        print("Please select a shape for area calculation:\n"
              "1 - rectangle\n"
              "2 - triangle\n"
              "3 - circle")

        i = int(input())

        match i:
            case 1:
                def rectangle_area(a, b):
                    """Function calculates the area of a rectangle where:
                    a = the length of the rectangle
                    b = the width of the rectangle
                    """
                    result = a * b
                    return result

                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = rectangle_area(length, width)
                print(f"The area of the rectangle is: {area}")
                break

            case 2:
                def triangle_area(a, h):
                    """Function calculates the area of a triangle where:
                    a = the length of the triangle's base
                    h = the length of the triangle's height
                    """
                    s = 0.5 * h * a
                    return s

                a = float(input("Enter the length of the triangle's base: "))
                h = float(input("Enter the length of the triangle's height: "))
                area = triangle_area(a, h)
                print(f"The area of the triangle is: {area}")
                break

            case 3:
                def circle_area(r):
                    """Function calculates the area of a circle where:
                    r = radius
                    """
                    result = pi * pow(r, 2)
                    return result

                radius = float(input("Enter the radius of the circle: "))
                area = circle_area(radius)
                print(f"The area of the circle is: {area}")
                break

            case _:
                print("Invalid choice. Please choose 1, 2, or 3.")


