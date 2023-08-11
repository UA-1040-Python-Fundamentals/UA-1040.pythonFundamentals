# Task №2

number = 6438
print("Задані чотиризначні числа:", number)
digit_product = 1
temp_number = number

while temp_number != 0:
    digit = temp_number % 10
    digit_product *= digit
    temp_number //= 10

print("Добуток цифр числа:", digit_product)

reversed_number = int(str(number)[::-1])
print("Число у зворотньому порядку:", reversed_number)

digit_list = {int(digit) for digit in str(number)}
sorted_digits =sorted(digit_list)
print("Числа у порядку зростання:", sorted_digits)
