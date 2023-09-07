temp = input()
if int(temp) < -273.15:
    print("Temperature is under absolute zero (-273.15)")
else:
    print((int(temp) * 9 / 5) + 32)