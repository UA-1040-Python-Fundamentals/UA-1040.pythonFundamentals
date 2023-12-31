import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < 10:
        try:
            guess = int(input("Take a guess: "))

            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == 10:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")


if __name__ == "__main__":
    guess_the_number()
