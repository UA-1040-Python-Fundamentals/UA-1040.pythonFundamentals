choice = int(input('What do you what to calculate? Write 1 for rectangle, 2 for triangle and 3 for circle: '))

if choice == 1:
    def rectangle(a, b):
        return a * b
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = rectangle(length, width)
    print(f"The area of the rectangle is: {area}")

elif choice == 2:
    def triangle(a, h):
        return 1 / 2 * a * h
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = triangle(base, height)
    print(f"The area of the triangle is: {area}")

elif choice == 3:
    def circle(r):
        return 3.14 * r * r
    radius = float(input("Enter radius: "))
    area = circle(radius)
    print(f"The area of the circle is: {area}")

else:
    print("Invalid choice")