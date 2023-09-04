def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n = int(input("Enter a non-negative integer: "))
    print(f"{n}! =", factorial(n))
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")