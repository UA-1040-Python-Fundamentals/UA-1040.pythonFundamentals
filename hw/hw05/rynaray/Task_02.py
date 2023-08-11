num = int(input("Enter a number: "))

fib_sequence = []
a, b = 0, 1
while a <= num:
    fib_sequence.append(a)
    a, b = b, a + b
print (fib_sequence)