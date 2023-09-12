def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter a number (n): "))

print("Fibonacci numbers up to", n, ":")
print_fibonacci(n)