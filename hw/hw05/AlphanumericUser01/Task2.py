# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number = int(input("please input number: "))
# number = 10
i = 0
step = 1
a = 0
fibonacci = 0
print("fibonacci numbers are: ", fibonacci, end=" ")
fibonacci = 1
while i < number:
    print(fibonacci, end=" ")
    fibonacci = a + step
    a = step
    step = fibonacci
    i += 1
