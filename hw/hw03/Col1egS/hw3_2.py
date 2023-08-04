num = int(input("Input four-digit natural number: "))
product = 1
numstr = num
num1 = num % 10
product = product * num1
num = num // 10
num1 = num % 10
product = product * num1
num = num // 10
num1 = num % 10
product = product * num1
num = num // 10
num1 = num % 10
product = product * num1
num = num // 10
print("Product of digits:", product)

numstr = str(numstr)
print("Reversed number:", numstr[::-1])

numstr = sorted(numstr)
print("Sorted number:", (''.join(numstr)))