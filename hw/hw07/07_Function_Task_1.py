'''Task1. Write a function that returns the largest number of two
numbers (use DocStrings documentation strings in the function).'''
def get_largest_num ():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if a > b:
        return a
    else:
        return b
largest_num = get_largest_num()
print("The largest number is: ", largest_num)