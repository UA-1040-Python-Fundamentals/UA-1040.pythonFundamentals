def largest_num(num1, num2) -> int:
    """
    The function takes two numbers and returns the greater of them
    """
    result = num1 if num1 > num2 else num2
    print(result)
    return result


largest_num(1, 7)
largest_num(1.25, 0.55)