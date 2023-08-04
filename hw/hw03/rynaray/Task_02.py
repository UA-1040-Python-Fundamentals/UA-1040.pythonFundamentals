number = input('Please input a four-digit natural number: ')

number_int = int(number)

thousands_digit = number_int // 1000
hundreds_digit = (number_int // 100) % 10
tens_digit = (number_int // 10) % 10
units_digit = number_int % 10

product = thousands_digit * hundreds_digit * tens_digit * units_digit

print(f'The product of the digits of this number is: {product}')

reversed_number = number[::-1]

print(f'The reversed number is: {reversed_number}')

digits_list = list(number)
digits_list.sort()
sorted_number = ''.join(digits_list)

print(f'This is a sorted number: {sorted_number}')