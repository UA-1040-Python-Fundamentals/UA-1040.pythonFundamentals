number = 3571

product = 1
for digit in str(number):
    product *= int(digit)

reversed_number = int(str(number)[::-1])

sorted_digits = ''.join(sorted(str(number)))

print(f"Number: {number}")
print(f"Product of digits: {product}")
print(f"Number in reverse order: {reversed_number}")
print(f"Digits in ascending order: {sorted_digits}")