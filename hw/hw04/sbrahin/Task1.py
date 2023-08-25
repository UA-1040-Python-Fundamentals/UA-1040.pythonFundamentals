userInput = input("Enter the temperature in Celsius: ")

if int(userInput) < -273.15:
  print("Eror.Temperature below absolute zero(-273.15°C)")
else :
  fahrenheit = (int(userInput)*9/5)+32
  print(f"{int(userInput)}°C is equivalent to {int(fahrenheit)}°F")
