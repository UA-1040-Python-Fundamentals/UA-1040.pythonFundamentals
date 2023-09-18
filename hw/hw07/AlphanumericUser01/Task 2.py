# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

from math import sqrt, pi

while True:
    print("Please choose what shape to calculate:\n"
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
            def triangle_area(a, b, c):
                """Function calculates the area of a triangle where:
                a, b, c = the length of the triangle sides
                """
                p = (a + b + c) / 2
                result = sqrt(p * (p - a) * (p - b) * (p - c))
                return result


            side1 = float(input("Enter the length of the first side of the triangle: "))
            side2 = float(input("Enter the length of the second side of the triangle: "))
            side3 = float(input("Enter the length of the third side of the triangle: "))
            area = triangle_area(side1, side2, side3)
            print(f"The area of the triangle is: {area}")
            break

        case 3:
            def circle_area(r):
                """Function calculates the area of a circle where:
                r = radius
                """
                result = pi * r ** 2
                return result


            radius = float(input("Enter the radius of the circle: "))
            area = circle_area(radius)
            print(f"The area of the circle is: {area}")
            break

        case _:
            print("Invalid choice. Please choose 1, 2, or 3.")
