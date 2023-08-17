# DESCRIPTION:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.


def multiple(num) -> list:
    """
    Accepts a number and returns a list of values that are multiples of 3 or 5 from natural values less than the specified number. If the number is a multiple and 3 and 5, the value is returned once. If the number passed is negative, 0 is returned
    """
    if num < 0: 
        return 0
    res_list = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            if i is res_list:
                continue
            else: res_list.append(i)
    return sum(res_list)

print(multiple(31))
print(multiple(-25))
