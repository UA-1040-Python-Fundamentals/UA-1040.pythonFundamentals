celsius = float(input("Введіть температуру у градусах Цельсія: "))
print ("Ви ввели" , celsius , "°C градусів Цельсія")
if celsius < -273.15:
    print("Помилка: температура нижче абсолютного нуля (-273,15°C)")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print("Градуси в Фарангейтах: ", fahrenheit, "°F")



