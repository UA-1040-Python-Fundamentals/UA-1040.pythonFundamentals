# Using the continue operator to print odd numbers less than 100
for num in range(1, 100, 2):
    if num % 2 == 0:
        continue
    print(num)

# Without using the continue operator to print odd numbers less than 100
for num in range(1, 100, 2):
    print(num)