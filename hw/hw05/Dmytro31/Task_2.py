n = int(input("Enter a number: "))

num1, num2 = 0, 1

print("Fibonacci sequence:", num1, num2, end=" ")

while num2 <= n:
    next_num = num1 + num2
    print(next_num, end=" ")
    num1, num2 = num2, next_num