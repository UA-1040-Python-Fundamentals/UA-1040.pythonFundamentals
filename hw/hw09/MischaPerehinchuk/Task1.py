import random

correct_answer = random.randint(1, 100)

attempts = 0

print("Welcome! You are playing the 'Guess the Number' game.")

while attempts < 10:
    attempts += 1
    user_guess = int(input("Attempt {}: Enter a number between 1 and 100: ".format(attempts)))

    if user_guess == correct_answer:
        print("Congratulations! You guessed the number {} in {} attempts!".format(correct_answer, attempts))
        break
    elif user_guess < correct_answer:
        print("Attempt {}: Try a higher number.".format(attempts))
    else:
        print("Attempt {}: Try a lower number.".format(attempts))

if attempts == 10:
    print("Sorry, you've used all 10 attempts. The correct answer was {}.".format(correct_answer))

print("Game over. Thank you for playing!")
