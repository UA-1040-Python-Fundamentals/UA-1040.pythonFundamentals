def print_fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib <= n:
            fib_sequence.append(next_fib)
        else:
            break

    print("Fibonacci numbers up to", n, ":", fib_sequence)

try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        print_fibonacci(n)
except ValueError:
    print("Invalid input. Please enter a valid non-negative number.")