while True:
    num = input("Enter four-digit natural number: ")

    # Перевірка чи число є чотирьохзначним та складається лише з цифр
    if not num.isdigit() or len(num) != 4:
        print("Please enter a valid four-digit number.")
    else:
        # Знаходження добутку цифр числа
        product = 1
        for digit in num:
            product *= int(digit)
        print("Product of digits:", product)

        # Виведення числа у зворотньому порядку
        reversed_num = num[::-1]
        print("Reversed number:", reversed_num)

        # Виведення числа у відсортованому порядку
        sorted_num = ''.join(sorted(num))
        print("Sorted number:", sorted_num)

        break  # Вихід із циклу, якщо число вірне

