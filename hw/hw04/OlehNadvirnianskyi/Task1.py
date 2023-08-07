celsius = float(input("Enter the temperature in Celsius:"))
fahrenheit = int((celsius * 9/5) + 32)
if celsius == -273.15 or celsius < -273.15:
    print("Temperature below absolute zero (-273.15°C)")
elif celsius in range(-273,15):
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")
else:
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")
git