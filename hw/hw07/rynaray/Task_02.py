import math

def rectangle_area(length, width):
    return length * width
def triangle_area(base, height):
    return 0.5 * base * height
def circle_area(radius):
    return math.pi * radius ** 2

print("Select a shape to calculate the area:\n"
      "1. Rectangle\n"
      "2. Triangle\n"
      "3. Circle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}")
else:
    print("Invalid choice!")

