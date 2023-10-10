# Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)

import random

number = random.randint(1, 100)
print(number)
for i in range(10):
    guess_number = int(input("Please enter the number: "))
    if guess_number == number:
        print("You are correct!")
        break
    elif guess_number < number:
        print("The entered number is less than the number in question")
    elif guess_number > number:
        print("The entered number is bigger than the number in question")

if number != guess_number:
    print(f"""The game is over :)
You have used your 10 tries""")
