def main():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        a = float(input("Enter the length of the rectangle (a): "))
        b = float(input("Enter the width of the rectangle (b): "))
        result = a * b
        print(f"The area of the rectangle is: {result}")
    elif choice == '2':
        h = float(input("Enter the height of the triangle (h): "))
        a = float(input("Enter the base of the triangle (a): "))
        result = 0.5 * h * a
        print(f"The area of the triangle is: {result}")
    elif choice == '3':
        r = float(input("Enter the radius of the circle (r): "))
        result = math.pi * math.pow(r, 2)
        print(f"The area of the circle is: {result}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()