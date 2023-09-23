#Print Fibonacci numbers up to the entered numbers n, using cycles.
#(Sequence of Fibonacci numbers 0,1,1,2,3,5,8,13, etc.)
# Function to print Fibonacci numbers up to n using loops
def print_fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    for num in fib_sequence:
        print(num, end=" ")

# Get input from the user
n = int(input("Enter a number: "))

print("Fibonacci numbers up to", n, ":")
print_fibonacci(n)