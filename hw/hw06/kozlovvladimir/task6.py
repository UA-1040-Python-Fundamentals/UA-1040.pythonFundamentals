#Task6.1
num = [num for num in range(1, 11)]

#determine even numbers that are divisible by 2
num1= [num1 for num1 in num if num1 %2 == 0]
#odd numbers, which are divisible by 3
num2= [num2 for num2 in num if num2 %3 == 0 and num2 % 2 != 0]
#numbers that are not divisible by 2 and 3
num3= [num3 for num3 in num if num3 % 2 != 0 and num3 % 3 != 0]



#Task6.2
login = input("Input login: ")
while login == "First":
    print("Hello)")
    break
else:
    print("Error")


