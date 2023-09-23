"""Write a program that calculates the area of a rectangle S=a*b, the area of a
triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
another module in which we ask the user the area of which figure he wants to
calculate.
(To perform the task, you need to import the math module, and from it the
pow() function and the value of the variable pi, and module, which contains
three functions for finding areas, into the main program. The basic logic of the
program is executed in the main module)."""

# main_program.py

import geometry_calculator

def main():
    print("Welcome to the Geometry Calculator!")
    print("Choose the figure whose area you want to calculate:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = geometry_calculator.rectangle_area(a, b)
        print(f"The area of the rectangle is: {area}")
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = geometry_calculator.triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = geometry_calculator.circle_area(radius)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()