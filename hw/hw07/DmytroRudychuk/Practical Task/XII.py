# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail) is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

# If the tail is right return true, else return false.

# The arguments will always be non-empty strings, and normal letters.

def correct_tail(body, tail):
    """
    Accepts two string values ​​and returns True if the last character of the first value matches the first character of the second value, otherwise False
    """

    return True if body[-1] == tail[0] else False


print(correct_tail("Fox", "x"))
print(correct_tail("Fox", "y"))