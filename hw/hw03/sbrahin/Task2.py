number = (input("Input four-digit natural number: "))

mult = 1
for digit in number:
    mult *= int(digit)
print(f"Product of digits:{mult}")

# Number in reverse order(string slicing method)
print(f"Number in reverse order:{(number)[::-1]}")

# Numbers in ascending order(sorted method)
print(f"Numbers in ascending order:{(''.join(sorted(str(number))))}")
