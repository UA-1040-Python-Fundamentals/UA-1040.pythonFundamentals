def largest(a, b):

 if a > b:
    return a
 else:
    return b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = largest(a, b)
print(f"The largest number is: {result}")