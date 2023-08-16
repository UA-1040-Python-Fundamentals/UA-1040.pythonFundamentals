# Write a script that will calculate the factorial of the entered number without using recursion
number = int(input("please input number: "))
d = 1
factorial = 1
if number == 0:
    print(1)
else:
    for i in range(number):
        factorial = factorial * (d)
        # print(factorial, end=" ")
        d += 1
print(f'''Factorial of {number} is''',factorial)