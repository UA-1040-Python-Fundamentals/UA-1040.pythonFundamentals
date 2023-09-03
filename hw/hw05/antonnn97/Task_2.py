def print_fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    print("Fibonacci numbers up to", n, ":", fib_sequence)

n = int(input("Enter a number: "))
print_fibonacci(n)