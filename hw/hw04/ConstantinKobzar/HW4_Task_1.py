def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        if celsius >= -273.15:
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F")
        else:
            print("Error: Temperature below absolute zero (-273.15°C)")
    except ValueError:
        print("Error: Invalid input. Please enter a valid temperature in Celsius.")

if __name__ == "__main__":
    main()