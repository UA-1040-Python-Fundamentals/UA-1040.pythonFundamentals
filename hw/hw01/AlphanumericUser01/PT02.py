# WRITE A PROGRAM THAT WILL CALCULATE THE SUM, DIFFERENCE, PRODUCT,
# EXPONENTIATION ETC. OF TWO NUMBERS A AND B THAT THE PROGRAM READS
# FROM THE CONSOLE (DATA ENTERED BY THE USER) AND WILL OUTPUT APPROPRIATE RESULT:
# "A + B = "  ...
# "A - B = "   ...
# "A * B = "   ...
# "A / B = "   ...
# "A**B = "   ...
# "A//B = "   ...
# "A%B = "  ...

A = float(input("Enter your number A: "))
B = float(input("Enter your number B: "))

sum = A + B
difference = A - B
product = A * B
division = A / B
exponentiation = A ** B
flour = A // B
modulo = A % B

print("A + B= ", sum)
print("A - B= ", difference)
print("A * B= ", product)
print("A / B= ", division)
print("A ** B= ", exponentiation)
print("A // B= ", flour)
print("A % B= ", modulo)