number = 9382


digit_1 = number % 10
digit_2 = (number // 10) % 10
digit_3 = (number // 100) % 10
digit_4 = (number // 1000) % 10

product = digit_1 * digit_2 * digit_3 * digit_4


print("Product of digits:", product)
print("Reverse number is ", int(str(number)[:: -1]))
print("Sorted number is ", int("".join(sorted(str(number)))))