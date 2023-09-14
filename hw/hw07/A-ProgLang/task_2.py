import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

while True:
    print("Оберіть опцію для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    print("4. Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        width = float(input("Введіть ширину прямокутника: "))
        height = float(input("Введіть висоту прямокутника: "))
        area = calculate_rectangle_area(width, height)
        print(f"Площа прямокутника: {area}")
    elif choice == '2':
        base = float(input("Введіть довжину основи трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = calculate_triangle_area(base, height)
        print(f"Площа трикутника: {area}")
    elif choice == '3':
        radius = float(input("Введіть радіус кола: "))
        area = calculate_circle_area(radius)
        print(f"Площа кола: {area}")
    elif choice == '4':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
