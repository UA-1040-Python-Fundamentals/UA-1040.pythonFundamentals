# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).

def larger_number(nm1, nm2):
    """function define the large number from 2 given numbers"""
    larger_nm = max(nm1, nm2)
    return larger_nm


number_1 = input("Please input number one: ")
number_2 = input("Please input number two: ")

print("The lager number is:", larger_number(number_1, number_2))

# print(larger_number.__doc__)