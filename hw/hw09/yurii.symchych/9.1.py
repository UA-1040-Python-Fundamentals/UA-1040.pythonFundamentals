import random

secret_number = random.randint(1, 100)

max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"Try to guess the secret number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:

        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("The secret number is greater than your guess.")
        else:
            print("The secret number is less than your guess.")

        if attempts == max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for playing!")