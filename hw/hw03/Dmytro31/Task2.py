number = 4734
product = 1
temp_number = number
while temp_number > 0:
    digit = temp_number % 10
    product *= digit
    temp_number //= 10
print("Product of digits:", product)


reverse_num = int(str(number)[::-1])
print("Number in reverse order:", reverse_num)


digits = [int(digit) for digit in str(number)]
sorted_digits = sorted(digits)
sorted_num = int(''.join(map(str, sorted_digits)))
print("Digits sorted in ascending order:", sorted_num)