# 1. Write a program that prompts the user to enter an integer and determines whether
# the number is even or odd, taking into account the case of entering incorrect data.

try:
    user_input = (input("Enter an integer: "))
    number = int(user_input)

    if number % 2 == 0:
        print("You number is even")
    elif number % 2 != 0:
        print("You number is odd")

except ValueError:
    print("Error: the data entered is not a number")

    