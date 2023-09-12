numbers = [2, 4, 7, 10, 12, 15, 20]

odd_found = False

for num in numbers:
    if num % 2 != 0:
        odd_found = True
        break

if odd_found:
    print("The list contains at least one odd number.")
else:
    print("The list does not contain any odd numbers.")
