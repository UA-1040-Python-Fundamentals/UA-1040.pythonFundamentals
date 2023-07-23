user_input = float(input("Pleas input your temperature in Celsius: "))

if user_input < -273.15:
    print("Error: The lowest possible temperature in the universe is -273.15 C")
elif user_input == -273.15:
    fahrenheit = (user_input * 9/5) + 32
    print(f"{user_input} C is equivalent to {fahrenheit} F. Is absolute zero")
else:
    fahrenheit = (user_input * 9/5) + 32
    print(f"{user_input} C is equivalent to {fahrenheit} F")