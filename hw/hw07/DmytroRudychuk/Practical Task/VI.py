# DESCRIPTION:
# In this kata you will create a function that takes in a list and returns a list with the reverse order.

def revers_list(lst) -> list:
    """
    Reverse values in the list
    """

    return list(reversed(lst))

print(revers_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))