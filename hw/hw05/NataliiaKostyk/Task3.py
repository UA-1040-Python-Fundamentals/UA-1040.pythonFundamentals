def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result = result * i
    return result


n = int(input("Enter a number: "))
print(f"The factorial of your number is", factorial(n))
