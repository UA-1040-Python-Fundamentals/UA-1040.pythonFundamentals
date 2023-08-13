# DESCRIPTION:
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def boolean_to_string(b) -> str:
    """
    Returns the string "Yes" for true or the string "No" for false.
    """
    return "Yes" if b is True else "No"

print(boolean_to_string(True))
print(boolean_to_string(False))