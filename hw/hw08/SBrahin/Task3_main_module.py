import Task3_calculation_module

print("Hello, sir. Which shape do you want to calculate the area of?"
        "\n Rectangle - 1"
        "\n Triangle - 2"
        "\n Circle - 3")

user_input = input("Enter your choice here: ")

if user_input == "1":
    data_lenght = float(input("Please, input lenght: "))
    data_width = float(input("Please, input width: "))
    area = round(Task3_calculation_module.rectangle(data_lenght, data_width),4)
    print(f"The area of a rectangle is - {area}")
elif user_input == "2":
    data_base = float(input("Please, input base: "))
    data_perpendecularHeight = float(input("Please, input perpendecular height: "))
    area = round(Task3_calculation_module.triangle(data_base, data_perpendecularHeight),4)
    print(f"The area of a triangle is - {area}")
elif user_input == "3":
    data_radius = float(input("Please, input radius: "))
    area = round(Task3_calculation_module.circle(data_radius), 4)
    print(f"The area of a circle is - {area}")
else:
    print("Invalid input!Try again.")
