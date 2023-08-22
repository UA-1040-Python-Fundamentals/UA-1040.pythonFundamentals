def find_largest(a, b):
    """
    This function takes two numbers as input and returns the largest number.
    """
    if a > b:
        return a
    else:
        return b


first_num = input("Please enter the first number: ")
second_num = input("Please enter the second number: ")

print(f"The largest number between {first_num} and {second_num} is {find_largest(first_num, second_num)}")
