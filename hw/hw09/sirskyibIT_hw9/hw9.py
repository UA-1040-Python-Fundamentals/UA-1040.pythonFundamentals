import random

user_name = input("Hello! What is your name?\n")

number = random.randint(1, 100)
print(f"Well, {user_name}, I am thinking of a number between 1 and 100.")

attempt_count = 0  
max_attempts = 11

while True:
    attempt_count += 1
    remaining_attempts = max_attempts - attempt_count

    if remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining.")

        guess_number = int(input("Take a guess! Enter your number: "))

        if guess_number == number:
            print(f"Good job, {user_name}! You are a winner!")
            break

        elif 1 <= guess_number <= 100 and guess_number < number:
            print("Your number is less.")

        elif 1 <= guess_number <= 100 and guess_number > number:
            print("Your number is more.")

        else:
            print("Your number is not in the range 1 to 100. Try again:)")

    else:
        print(f"Sorry, {user_name}! You ran out of attempts. The number I was thinking of was {number}.")
        break
