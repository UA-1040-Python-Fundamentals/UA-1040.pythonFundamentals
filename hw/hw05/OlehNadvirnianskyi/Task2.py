fibo= int(input("Enter number:"))
for x in range(0,fibo):
    if x == 0:
        print(0)
    elif x == 1:
        print(1)
    else:
        print((x-2)+(x-1))
