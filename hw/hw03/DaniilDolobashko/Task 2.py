number = (input("Input four-digit natural number: "))
number_str = str(number)
product = 1
for digit in number_str:
    product *= int(digit)
print("Product of digits:", product)

print("Reversed number:", (number)[::-1])

digits = list(number_str)
sorted_digits = sorted(digits)
print("Sorted number:", (''.join(sorted_digits)))