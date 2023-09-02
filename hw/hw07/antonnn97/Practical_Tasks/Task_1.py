def find_largest_number(a, b):
    """ This functions returns the largest number between two given numbers. """
    return max(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = find_largest_number(num1, num2)
print(f"The largest number between {num1} and {num2} is: {result}")