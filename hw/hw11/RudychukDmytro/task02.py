# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.


class UserInputError(Exception):
    pass

def check(number):
    num = int(number)

    if num % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")

try:
    number = input("Enter your age: ")
    num = int(number)
    if num <= 0:
        raise UserInputError("Age must be a positive integer")
    check(num)
except ValueError:
    print("Error: Please enter a valid integer for age.")
except UserInputError as e:
    print(f"Error: {e}")
