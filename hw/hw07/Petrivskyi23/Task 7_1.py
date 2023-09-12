def find_largest_number(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

largest = find_largest_number(num1, num2)
print("The largest number is:", largest)