def find_max(a, b):
    """
    This function takes two numbers and returns the greater of the two.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The greater of the two numbers.
    """
    if a > b:
        return a
    else:
        return b


result = find_max(10, 5)
print(result)
print(find_max.__doc__)


