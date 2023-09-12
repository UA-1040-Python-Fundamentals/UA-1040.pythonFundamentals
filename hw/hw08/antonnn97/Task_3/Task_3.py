import geometry_calculator

print("Geometry Calculator")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter the number of the shape you want to calculate the area for: "))

if choice == 1:
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))
    area = geometry_calculator.rectangle_area(a, b)
    print(f"The area of the rectangle is {area}")
elif choice == 2:
    h = float(input("Enter the height of the triangle: "))
    a = float(input("Enter the base length of the triangle: "))
    area = geometry_calculator.triangle_area(h, a)
    print(f"The area of the triangle is {area}")
elif choice == 3:
    r = float(input("Enter the radius of the circle: "))
    area = geometry_calculator.circle_area(r)
    print(f"The area of the circle is {area}")
else:
    print("Invalid choice. Please select a valid option (1, 2, or 3).")