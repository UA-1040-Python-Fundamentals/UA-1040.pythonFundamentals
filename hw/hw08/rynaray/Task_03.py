import math

def rectangle_area(a, b):
    return a * b

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * math.pow(radius, 2)

if __name__ == "__main__":
    print("Select a shape to calculate the area:\n"
          "1. Rectangle\n"
          "2. Triangle\n"
          "3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        a, b = map(float, input("Enter the length and width of the rectangle: ").split())
        result = rectangle_area(a, b)
    elif choice == "2":
        base, height = map(float, input("Enter the base and the height of the triangle: ").split())
        result = triangle_area(base, height)
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        result = circle_area(radius)
    else:
        print("Invalid choice.")

    print(f"The area of the chosen figure: {result}")
