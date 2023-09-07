a, b = 0, 1
n = int(input("Enter a number: "))

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
