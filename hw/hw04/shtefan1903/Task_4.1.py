temp_c = int(input("Enter the temperature in Celsius: "))
convert_temp_f = (temp_c * 9/5) + 32
if temp_c > -273.15:
    print(temp_c,  chr(186) + "C", "is equivalent to", int(convert_temp_f), "in", chr(186) + "F" )
else:
    print("Error: Temperature below absolute zero (-273.15ºC)")
# for i in range(500):
#     print(i, ":", chr(i))