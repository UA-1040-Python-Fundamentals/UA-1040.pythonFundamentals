# Guess THE Number
import random

tries = 0

print('Let`s Play A Game. What is your name adventurer? : ')

name = input()

number = random.randint(1, 100)

print(f'So let`s get started then?,{name} I guessed a number from one to 100. You have only 10 attempts')

while tries < 10:
    guess = input()
    guess = int(guess)
    tries = tries+1
    if guess < number:
        print('My number is greater than yours')
    if guess > number:
        print('My number is less than yours')
    if guess == number:
        break
if guess == number:
    tries = str(tries)
    print(f'Excellent {name}! You guessed the number with a {tries} attempt. Congratulations!')
if guess != number:
    number = str(number)
    print(f'Sorry, but you have no more attempts. I guessed the number {number}. You lost...')
