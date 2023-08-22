def find_largest_number(num1, num2):

    if num1 > num2:
        return num1
    else:
        return num2


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
largest_number = find_largest_number(number1, number2)
print("The largest number is:", largest_number)