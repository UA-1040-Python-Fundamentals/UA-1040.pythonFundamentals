def find_largest_number(a, b):
    """
    Finds and returns the largest number between two given numbers.

    Parameters:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The largest number between a and b.
    """
    if a >= b:
        return a
    else:
        return b