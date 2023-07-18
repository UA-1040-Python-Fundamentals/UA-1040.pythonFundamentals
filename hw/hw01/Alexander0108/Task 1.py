
# Ствернная функції запитань та відповідей на них
def answer():
    # Створення нескінчненного циклу до тих пір, поки параметр agreement не набуде необхідного значення
    while True:
        name = input("What's your name?\n Enter your name: ")
        age = int(input("How old are you?\n Enter your age: "))
        locations = input("Where do you live?\n Enter your location: ")
        print(f"\nWell, hello {name}!")
        print(f"Your age is {age}")
        print(f"And you live in {locations}")
        agreement = input("Right?\n Write 'yes' or 'no': ")
        # Цикл перевірки користувачем правильності введених данних
        if agreement == 'yes':
            print("Great! We can continue our work...")
            exit()
        else:
            print("Let's double-check what doesn't match")
            continue

answer()