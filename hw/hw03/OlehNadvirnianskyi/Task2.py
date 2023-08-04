number = int(input("Enter a four-digit natural number: "))
num1= number//1000
num2= number//100%10
num3= number//10%10
num4= number%10
digit= num1*num2*num3*num4
print("The product of the digits of numbers:", digit)
print("Reverse order:",str(number)[::-1])
sort= sorted(str(number))
print("Ascending order:",''.join(sort))