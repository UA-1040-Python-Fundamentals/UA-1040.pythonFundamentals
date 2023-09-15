from random import randint

number = randint(1, 100)
tries = 0

print("Welcome to the guessing game!")
print("I have chosen a number between 1 and 100. You have 10 tries to guess it.")

while True:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess == number:
        print(f"Congratulations! You guessed it in {tries} tries.")
        break
    elif guess > number:
        print("The number is greater. Try again.")
    elif guess < number:
        print("The number is less. Try again.")
    if tries == 10:
        print(f"Sorry, you ran out of tries. The number was {number}.")
        break
