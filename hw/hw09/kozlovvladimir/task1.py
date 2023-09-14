
from random import randint


def game_script():

    number = randint(1, 100)
    attempts = 0

    while attempts < 10:
        answer = int(input("Аsk the user to guess that number: "))
        attempts += 1
        if answer == number:
            print(f"You guessed the number {answer} in {number} .")
            break
        elif answer < number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    if attempts == 10:
        print(f"Game over.")

if __name__ == "__main__":
    game_script()






