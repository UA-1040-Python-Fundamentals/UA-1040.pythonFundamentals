f = "-273.15"
absolute_zero = float(f)

while True:
    celsius = float(input("Enter the temperature in Celsius:"))

    if celsius <= absolute_zero:
        print("Temperature below absolute zero", absolute_zero)
        break
    else:
        fahrenheit = (celsius * 9/5) + 32
        print("%s C is equivalent to %s F" % (celsius, fahrenheit))