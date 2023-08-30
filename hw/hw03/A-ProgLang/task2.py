number = 1354
number_str = str(number)
#product of the digits
digit_1 = int(number_str[0])
digit_2 = int(number_str[1])
digit_3 = int(number_str[2])
digit_4 = int(number_str[3])
product = digit_1 * digit_2 * digit_3 * digit_4
print ("Product of the numbers", product)
#reverse order
reversed_number_str = number_str[::-1]
reversed_number = int(reversed_number_str)
print("The reverse order of the number", reversed_number)
#ascending order
sorted_digits = sorted(number_str)
sorted_number = int(''.join(sorted_digits))
print("Number in ascending order", sorted_number)