import area_module

while True:
    user_choice = input("""Which shape do you want to calculate the area of?
    (rectangle, triangle or circle): """)
    user_choice = user_choice.lower()
    if user_choice == 'rectangle':
        length = float(input("Enter the length of the rectangle in centimeters: "))
        width = float(input("Enter the width of the rectangle in centimeters: "))
        print(f"The area of the rectangle is {area_module.rectangle_area(length, width)} square centimeters.")
        break
    elif user_choice == 'triangle':
        base = float(input("Enter the base of the triangle in centimeters: "))
        height = float(input("Enter the height of the triangle in centimeters: "))
        print(f"The area of the triangle is {area_module.triangle_area(base, height)} square centimeters.")
        break
    elif user_choice == 'circle':
        radius = float(input("Enter the radius of the circle in centimeters: "))
        print(f"The area of the circle is {area_module.circle_area(radius)} square centimeters.")
        break
    else:
        print("Invalid shape. Please enter rectangle, triangle or circle.")
