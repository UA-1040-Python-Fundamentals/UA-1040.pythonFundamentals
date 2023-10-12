# Write a function that returns the arithmetic mean of any number of numbers.

def arithmetic_mean(*numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    mean = total / len(numbers)
    return mean


numbers = [10, 20, 30, 40, 50]
result = arithmetic_mean(*numbers)
print(f"The arithmetic mean of {numbers} is {result}")
