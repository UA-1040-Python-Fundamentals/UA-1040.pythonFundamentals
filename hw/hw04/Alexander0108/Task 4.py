# Task 4.1
print("Checking equality of values")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    print(f"First number - {x}, is bigger than second number - {y}")
elif x < y:
    print(f"First number - {x}, is less than second number - {y}")
else:
    print("The numbers are equal to")

# Task 4.2

print("Checking a number for parity")

x = int(input("Enter the number: "))

if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Task 4.3

print("Converting degrees Celsius (°C) to Fahrenheit (°F)")

temperature = float(input("Enter the temperature value you want to convert: "))

match temperature:
    case x if temperature >= (-273.15):
        print(f"If we convert the value of {x}°C into Fahrenheit, we get - {x*(9/5)+32}°F")
    case _ :
        print("Temperature below absolute zero (-273.15°C)")