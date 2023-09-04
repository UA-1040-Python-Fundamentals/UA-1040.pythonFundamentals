def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))

if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15 °C)")
else:
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f} °C is equivalent to {fahrenheit:.2f} °F")