C = float(input('Enter the temperature in Celsius: '))
F = (C * 9/5) + 32
print((C > -273.15) and (f'{C}°C is equivalent to {F:.2f}°F') or (f'Error: Temperature below absolute zero ({C}°C)'))