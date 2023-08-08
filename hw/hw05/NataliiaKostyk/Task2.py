n = int(input("Enter your number: "))

n1, n2 = 0, 1

if n == 1:
    print(n1)
else:
    print("Fibonacci sequence: ")

while n1 < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
