def largest_number(first_num, second_num):
    """
    Returns the largest number of two given numbers.
    """
    if first_num >= second_num:
        return first_num
    else:
        return second_num

#Example
first_num = 15
second_num = 2
print(f"The largest number between {first_num} and {second_num} is {largest_number(first_num, second_num)}")