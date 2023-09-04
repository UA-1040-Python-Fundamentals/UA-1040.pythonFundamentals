C = int(input("Enter temperature in Celsius: "))
if C < -273.15:
    print("Error. You entered temperature less than the lowest possible temperature in the universe")
else:
    F = (C * 9/5) + 32
    print(f"{C}°C is equivalent to {F}°F")
