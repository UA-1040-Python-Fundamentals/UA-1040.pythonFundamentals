import random

guess_number = random.randint(1, 100)
attempts = 0

print("I have chosen a number between 1 and 100. Guess it in 10 tries.")

while attempts < 10:
    try:
        guess = int(input(f"Attempt {attempts + 1}/10 - Enter your guess: "))
    except ValueError:
        print("Your number is invalid.")
        continue
    attempts += 1

    if guess < guess_number:
        print("The number is higher.")
    elif guess > guess_number:
        print("The number is lower.")
    else:
        print(f"Congratulations! You have guessed the number {guess_number} in {attempts} attempts!")
        break

if attempts == 10 and guess != guess_number:
    print(f"Ha-ha, you lost! The number was {guess_number}.")
