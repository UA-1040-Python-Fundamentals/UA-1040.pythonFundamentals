celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

if celsius >= -273.15:
    print(f"{celsius} degree Celsius is equal to {fahrenheit:.2f} degree Fahrenheit")
else:
    print("Error: Temperature below absolute zero (-273.15 degree Celsius)")