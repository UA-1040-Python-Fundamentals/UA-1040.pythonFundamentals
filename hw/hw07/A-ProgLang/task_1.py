#Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).

def find_largest_number(a, b):
    """
    Find the largest number between two given numbers.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The largest number between `a` and `b`.

    Examples:
        >>> find_largest_number(5, 10)
        10
        >>> find_largest_number(-3, -7)
        -3
        >>> find_largest_number(3.5, 3.5)
        3.5
    """
    return max(a, b)

number1 = 25
number2 = 18
largest = find_largest_number(number1, number2)
print(f"The largest number between {number1} and {number2} is {largest}")