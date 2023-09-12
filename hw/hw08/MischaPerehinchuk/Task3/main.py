from calculate_area import rectangle_area, triangle_area, circle_area

def calculate():
    print("Обчислення площі фігур:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = int(input("Виберіть фігуру (1/2/3): "))

    if choice == 1:
        a = float(input("Введіть довжину сторони 'а': "))
        b = float(input("Введіть довжину сторони 'b': "))
        area = rectangle_area(a,b)
        print(f"Площа прямокутника зі сторонами {a} та {b} дорівнює {area}")
    elif choice == 2:
        base = float(input("Введіть довжину основи трикутника:"))
        height = float(input("Введіть висоту трикутника:"))
        area = triangle_area(base,height)
        print(f"Площа трикутника з основою {base} і висотою {height} дорівнює {area}")
    elif choice == 3:
        radius = float(input("Введіть радіус кола: "))
        area = circle_area(radius)
        print(f"Площа кола з радіусом {radius} дорівнює {area}")
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    calculate()
