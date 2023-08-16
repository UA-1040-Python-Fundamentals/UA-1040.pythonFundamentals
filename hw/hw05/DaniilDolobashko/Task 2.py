n = int(input("Enter the number of digits that you want in the Fibonacci sequence: "))
n1, n2 = 0, 1
count = 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci sequence up to n terms will be: {n1}")

else:
    print("Fibonacci sequence up to n terms will be: ")
    while count <= n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
