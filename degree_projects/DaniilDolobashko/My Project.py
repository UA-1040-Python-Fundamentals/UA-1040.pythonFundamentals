import re

cart = []

# Функції та класи
cart_sum = 0
def add_to_cart(product, amount_of_products):
    global cart_sum
    cart_sum += product.price * amount_of_products
    cart.append((product, amount_of_products))
    print(f"{product.name} було додано до кошику у кількості {amount_of_products} шт.")

amount_of_products = 0
def amount_counter():
    global amount_of_products
    while True:
        amount_of_products = input("Виберіть кількість (введіть ціле число від 1 до 9): ")

        if amount_of_products.isdigit():
            amount_of_products = int(amount_of_products)
            if 1 <= amount_of_products <= 9:
                break
            else:
                print("Кількість має бути від 1 до 9.")
        else:
            print("Помилка вводу.")

def payment():
    try:
        if cart_sum == 0:
            print("Спочатку додайте товари то кошика.")
        else:
            print(f"До сплати: {cart_sum}")
            pay_choice = int(input("Оберіть метод оплати:\n"
                                   "1 - Оплата при отриманні\n"
                                   "2 - Оплатити онлайн\n"))

            if pay_choice == 1:
                print("Добре, очікуйте на доставку!")
            elif pay_choice == 2:
                print("Будь ласка, введіть дані вашої картки.")
                while True:
                    try:
                        card_number = input("Номер: ")
                        if len(card_number) != 16:
                            print("Ви ввели неправильну кількість цифр. Будь ласка, введіть 16 цифр.")
                        else:
                            break
                    except ValueError:
                        print("Помилка вводу. Будь ласка, введіть ціле число.")

                while True:
                    card_date = input("Введіть термін дії в наступному форматі ХХ/ХХ: ")
                    match = re.match(r'\d{2}/\d{2}', card_date)
                    if match:
                        break
                    else:
                        print("Неправильний формат email адреси. Будь ласка, спробуйте ще раз.")

                while True:
                    try:
                        card_cvv = input("CVV: ")
                        if len(card_cvv) != 3:
                            print("Ви ввели неправильну кількість цифр. Будь ласка, введіть 3 цифри.")
                        else:
                            break
                    except ValueError:
                        print("Помилка вводу. Будь ласка, введіть ціле число.")
                print("Оплачено! Очікуйте на доставку!")
            else:
                print("Невірне значення.")
    finally:
        pass

class SpinningRod:
    def __init__(self, name, price, weight, length, test):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length
        self.test = test

spinning_rods = [
    SpinningRod("Dagger легкий", 977, 118, 2.10, "3-17"),
    SpinningRod("Dagger сердній", 1005, 128, 2.10, "5-25"),
    SpinningRod("Dagger важкий", 1070, 136, 2.10, "10-35"),
    SpinningRod("Larva легкий", 1654, 89, 2.13, "0.5-6"),
    SpinningRod("Larva середній", 1774, 103, 2.38, "2-12"),
    SpinningRod("Larva важкий", 1918, 116, 2.55, "3-15"),
    SpinningRod("Lexus легкий", 1506, 140, 2.65, "8-28"),
    SpinningRod("Lexus середній", 1506, 148, 2.65, "9-39"),
    SpinningRod("Lexus важкий", 1506, 146, 2.65, "15-50")
]

class FeederRod:
    def __init__(self, name, price, weight, length, test):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length
        self.test = test

feeder_rods = [
    FeederRod("Egoist легкий", 1787, 270, 3.60, "90"),
    FeederRod("Egoist сердній", 1911, 290, 3.60, "120"),
    FeederRod("Egoist важкий", 1962, 295, 3.60, "150"),
    FeederRod("Gorizont легкий", 2890, 355, 3.60, "150"),
    FeederRod("Gorizont середній", 2990, 385, 3.60, "180"),
    FeederRod("Gorizont важкий", 3550, 475, 3.60, "200"),
    FeederRod("Gorizont екстраважкий", 3990, 605, 3.60, "250"),
    FeederRod("Pulemet легкий", 948, 275, 3, "90"),
    FeederRod("Pulemet середній", 979, 245, 3, "120"),
    FeederRod("Pulemet важкий", 1077, 308, 3, "150")
]

class FloatRod:
    def __init__(self, name, price, weight, length, test):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length
        self.test = test

float_rods = [
    FloatRod("Raketa Ballerina коротка", 1168, 257, 5, "10-25"),
    FloatRod("Raketa Ballerina середня", 1272, 335, 6, "10-25"),
    FloatRod("Raketa Ballerina довга", 1357, 345, 7, "10-25"),
    FloatRod("Lexus короткий", 1259, 199, 5, "10-30"),
    FloatRod("Lexus середній", 1631, 285, 6, "10-30"),
    FloatRod("Lexus довгий", 2100, 403, 7, "10-30"),
    FloatRod("Rapira коротка", 1470, 195, 3.6, "10-35"),
    FloatRod("Rapira середня", 1631, 193, 4, "10-35"),
    FloatRod("Rapira довга", 1909, 267, 4.5, "10-35")
]

class CoilsForFishingRod:
    def __init__(self, name, price, weight, bearing, braking_effort):
        self.name = name
        self.price = price
        self.weight = weight
        self.bearing = bearing
        self.braking_effort = braking_effort

coils = [
    CoilsForFishingRod("Solist 4000 безінерційна", 3002, 318, "5+1", 4.5),
    CoilsForFishingRod("Solist 3000 безінерційна", 2911, 304, "5+1", 4.5),
    CoilsForFishingRod("Major 4000 безінерційна", 1811, 252, "9+1", 11),
    CoilsForFishingRod("Major 3000 безінерційна", 1777, 245, "9+1", 11),
    CoilsForFishingRod("Riga 5000 безінерційна с бейтранером", 1802, 483, "5+1", "7/5"),
    CoilsForFishingRod("Riga 4000 безінерційна с бейтранером", 1748, 352, "5+1", "5/2.5"),
    CoilsForFishingRod("Riga 3000 безінерційна с бейтранером", 1695, 332, "5+1", "5/2.5")
]

class FishingLine:
    def __init__(self, name, price, diameter, length, test):
        self.name = name
        self.price = price
        self.diameter = diameter
        self.length = length
        self.test = test

lines = [
    FishingLine("Волосінь Невидимка", 67.70, 0.12, 100, 3.1),
    FishingLine("Волосінь Невидимка", 67.70, 0.14, 100, 4),
    FishingLine("Волосінь Невидимка", 67.70, 0.16, 100, 4.7),
    FishingLine("Волосінь Невидимка", 67.70, 0.18, 100, 5.5),
    FishingLine("Super Jig PE X8", 627, 0.10, 150, 4.8),
    FishingLine("Super Jig PE X8", 423, 0.12, 150, 6.9),
    FishingLine("Super Jig PE X8", 423, 0.14, 150, 8.8)
]


# Магазин
print("Вітаємо у нашому риболовному магазині \"Рибник\"!")
print("Давайте пройдемо реєстрацію")

while True:
    name = input("Введіть своє прізвище та ім'я: ")
    if len(name) < 10:
        print("Ви ввели замало символів. Будь ласка, спробуйте ще раз.")
    else:
        break

while True:
    try:
        number = input("Введіть Ваш номер телефону: ")
        number_str = str(number)
        if len(number_str) != 10:
            print("Ви ввели неправильну кількість цифр. Будь ласка, введіть 10 цифр.")
        else:
            break
    except ValueError:
        print("Помилка вводу. Будь ласка, введіть ціле число.")

while True:
    email = input("Введіть Вашу email адресу: ")
    match = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+', email)
    if match:
        print("Реєстрація пройшла успішно!")
        break
    else:
        print("Неправильний формат email адреси. Будь ласка, спробуйте ще раз.")

while True:
    print("Меню:")
    print("1. Перейти до вибору товару")
    print("2. Перейти до кошика")
    print("3. Зробити замовлення")
    print("4. Покинути магазин")

    menu_choice = input("Введіть ваш вибір: ")

    if menu_choice == "1":
        print("Який товар вас цікавить?")
        print("1. Спінінги")
        print("2. Фідерні вудилища")
        print("3. Поплавцеві вудилища")
        print("4. Котушки")
        print("5. Шнури та волосінь")
        product_choice = input("Введіть ваш вибір: ")

        if product_choice == "1":
            while True:
                print("Ось товари у категорії cпінінги:")
                for i, rod in enumerate(spinning_rods):
                    print(f"{i + 1}. Назва: {rod.name}, Ціна: {rod.price} грн, Вага: {rod.weight} г, Довжина: {rod.length} м, Тест: {rod.test}")
                choice_of_product = input("Виберіть товар, який ви хочете додати до корзини (введіть номер товару або 'q' щоб повернутися назад): ")
                if choice_of_product.isdigit() and 1 <= int(choice_of_product) <= len(spinning_rods):
                    selected_rod = spinning_rods[int(choice_of_product) - 1]
                    amount_counter()
                    add_to_cart(selected_rod, amount_of_products)
                elif choice_of_product == 'q':
                    break
                else:
                    print("Помилка вводу.")

        elif product_choice == "2":
            print("Ось товари у категорії фідерні вудилища:")
            while True:
                for i, rod in enumerate(feeder_rods):
                    print(f"{i + 1}. Назва: {rod.name}, Ціна: {rod.price} грн, Вага: {rod.weight} г, Довжина: {rod.length} м, Тест: {rod.test}")
                choice_of_product = input("Виберіть товар, який ви хочете додати до корзини (введіть номер товару або 'q' щоб повернутися назад): ")
                if choice_of_product.isdigit() and 1 <= int(choice_of_product) <= len(feeder_rods):
                    selected_rod = feeder_rods[int(choice_of_product) - 1]
                    amount_counter()
                    add_to_cart(selected_rod, amount_of_products)
                elif choice_of_product == 'q':
                    break
                else:
                    print("Помилка вводу.")

        elif product_choice == "3":
            print("Ось товари у категорії поплавцеві вудилища:")
            while True:
                for i, rod in enumerate(float_rods):
                    print(f"{i + 1}. Назва: {rod.name}, Ціна: {rod.price} грн, Вага: {rod.weight} г, Довжина: {rod.length} м, Тест: {rod.test}")
                choice_of_product = input("Виберіть товар, який ви хочете додати до корзини (введіть номер товару або 'q' щоб повернутися назад): ")
                if choice_of_product.isdigit() and 1 <= int(choice_of_product) <= len(float_rods):
                    selected_rod = float_rods[int(choice_of_product) - 1]
                    amount_counter()
                    add_to_cart(selected_rod, amount_of_products)
                elif choice_of_product == 'q':
                    break
                else:
                    print("Помилка вводу.")


        elif product_choice == "4":
            print("Ось товари у категорії котушки:")
            while True:
                for i, coil in enumerate(coils):
                    print(
                        f"{i + 1}. Назва: {coil.name}, Ціна: {coil.price} грн, Вага: {coil.weight} г, Кількість підшипників: {coil.bearing}, Гальмівне зусилля: {coil.braking_effort} кг")
                choice_of_product = input("Виберіть товар, який ви хочете додати до корзини (введіть номер товару або 'q' щоб повернутися назад): ")
                if choice_of_product.isdigit() and 1 <= int(choice_of_product) <= len(coils):
                    selected_coil = coils[int(choice_of_product) - 1]
                    amount_counter()
                    add_to_cart(selected_coil, amount_of_products)
                elif choice_of_product == 'q':
                    break
                else:
                    print("Помилка вводу.")

        elif product_choice == "5":
            print("Ось товари у категорії шнури та волосінь:")
            while True:
                for i, line in enumerate(lines):
                    print(f"{i + 1}. Назва: {line.name}, Ціна: {line.price} грн, Довжина: {line.length} м, Діаметр: {line.diameter} мм, Тест: {line.test} кг")
                choice_of_product = input("Виберіть товар, який ви хочете додати до корзини (введіть номер товару або 'q' щоб повернутися назад): ")
                if choice_of_product.isdigit() and 1 <= int(choice_of_product) <= len(lines):
                    selected_line = lines[int(choice_of_product) - 1]
                    amount_counter()
                    add_to_cart(selected_line, amount_of_products)
                elif choice_of_product == 'q':
                    break
                else:
                    print("Помилка вводу.")

        else:
            print("Помилка вводу.")



    elif menu_choice == "2":
        print("Вітаємо у кошику. Ось товари, які ви додали: ")
        for i, (product, quantity) in enumerate(cart):
            if isinstance(product, CoilsForFishingRod):
                print(f"{i + 1}. {product.name}, Ціна: {product.price} грн, Вага: {product.weight} г, Кількість підшипників: {product.bearing}, Гальмівне зусилля: {product.braking_effort} кг, Кількість: {quantity} шт.")
            elif isinstance(product, FishingLine):
                print(f"{i + 1}. Назва: {product.name}, Ціна: {product.price} грн, Вага: {product.length} м, Діаметр: {product.diameter} мм, Тест: {product.test} кг")
            else:
                print(f"{i + 1}. {product.name}, Ціна: {product.price} грн, Вага: {product.weight} г, Довжина: {product.length} м, Тест: {product.test}, Кількість: {quantity} шт.")
        print(f"Загальна вартість товарів: {cart_sum}")

    elif menu_choice == "3":
        print("Оформлення замовлення\n")
        delivery_choice = int(input("Оберіть метод доставки:\n"
                                    "1 - Самовивіз з магазину (Київ) - безкоштовно\n"
                                    "2 - Доставка кур'єром - 100 грн\n"
                                    "3 - Доставка Новою Поштою - 80 грн\n"
                                    "4 - Доставка Укрпоштою - 50 грн\n"
                                    "Ваш вибір: "))

        if delivery_choice == 1:
            print("Наш магазин знаходиться в Києві за адресою: Сагайдачного вул., 51.")
            print("Графік роботи: Пн-Пт - 10:00-18:00")
            payment()

        elif delivery_choice == 2:
            delivery_address = input("Введіть адресу доставки: ")
            delivery_time = int(input("О котрій годині завтра вам буде зручно отримати замовлення?"))
            print(f"{name}, очійкуйте нашого кур'єра завтра близько {delivery_time} години")
            payment()

        elif delivery_choice == 3:
            department = input("Введіть номер відділення: ")
            print(f"{name}, очікуйте ваше замовлення в {department} відділенні!")
            payment()

        elif delivery_choice == 4:
            department = input("Введіть номер відділення: ")
            print(f"{name}, очікуйте ваше замовлення в {department} відділенні!")
            payment()

        else:
            print("Невірне значення.")

    elif menu_choice == "4":
        print("Дякуємо, що ви відвідали наш магазин!")
        break
    else:
        print("Помилка вводу.")