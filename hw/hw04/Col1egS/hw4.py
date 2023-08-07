C = int(input("Enter the temperature in Celsius: "))
if C < -273.15:
    print("Temperature below absolute zero (273.15)!!!")
else:
    F = (C * (9/5)+32)
    print(f"{C}°C is equivalent to {int(F)}°F")