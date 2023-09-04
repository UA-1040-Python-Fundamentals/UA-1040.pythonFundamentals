a = float(input("Enter the first number (A): "))
b = float(input("Enter the second number (B): "))

sum_result = a + b
difference_result = a - b
multiplication_result = a * b
division_result = a / b
exponentiation_result = a ** b
floor_division = a // b
modulus_result = a % b

print("A + B =", sum_result)
print("A - B =", difference_result)
print("A * B =", multiplication_result)
print("A / B =", round(division_result, 2))
print("A ** B =", exponentiation_result)
print("A // B =", floor_division)
print("A % B =", modulus_result)
