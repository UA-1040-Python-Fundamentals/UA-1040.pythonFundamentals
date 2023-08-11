#HW-05.1


my_list = [1,2,3,4,5,6]
for i in my_list:
    if my_list is list:
        print(i)
    else:
        print(float(i))
print("end")

#HW-05.2

number = int(input("Enter the number to which you want to hit the Fibonacci number: "))
if number <= 0:
    print("Please enter a number greater than 0")
else:
    number1 = 0
    number2 = 1

    for i in range(number):
        if number1 > number:
            break
        else:
            print(number1)
            number1,number2 = number2, number1+number2
print("End")


# HW-05.3