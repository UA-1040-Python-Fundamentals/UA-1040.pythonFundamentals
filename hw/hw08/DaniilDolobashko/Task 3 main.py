import Task_3_area_calculator

while True:
    print("Choose a shape to calculate its area:")
    print("Write 1 for Rectangle")
    print("2 for Triangle")
    print("3 for Circle")

    choice = input("Enter your choice: ")

    if choice == '1':
        a = float(input("Enter the width of the rectangle: "))
        b = float(input("Enter the height of the rectangle: "))
        area = Task_3_area_calculator.rectangle(a, b)
        print(f"The area of the rectangle is: {area}")
        break

    elif choice == '2':
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = Task_3_area_calculator.triangle(a, h)
        print(f"The area of the triangle is: {area}")
        break

    elif choice == '3':
            r = float(input("Enter the radius of the circle: "))
            area = Task_3_area_calculator.circle(r)
            print(f"The area of the circle is: {area}")
            break

    else:
        print("Invalid choice. Please select a valid option.")

