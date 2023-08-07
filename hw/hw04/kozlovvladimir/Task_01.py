temperature = float(input("Pleas input your temperature in Celsius:\n "))
if temperature < -273.15:
    print("Error: The lowest possible temperature in the universe is -273.15 C")
elif temperature == -273.15:
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature} C is equivalent to {fahrenheit} F. Is absolute zero")
else:
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature} C is equivalent to {fahrenheit} F")
