import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number (between 1 and 100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("The secret number is greater. Try again.")
    else:
        print("The secret number is smaller. Try again.")

if attempts == max_attempts and guess != secret_number:
    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}")