n = int(input("Please enter the number: "))
fibonnaci_num = [0, 1]

for i in fibonnaci_num:
    print(i)
    if fibonnaci_num[-1]+fibonnaci_num[-2] < n:
        fibonnaci_num.append(fibonnaci_num[-1]+fibonnaci_num[-2])
