C = float(input('Enter the temperature in Celsius: '))
F = (C * 9/5) + 32

converted_temperature = F

if C < -273.13:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    print(f"{C}°C is equivalent to {converted_temperature}°F")
