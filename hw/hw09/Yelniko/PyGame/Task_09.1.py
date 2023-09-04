from random import randint


def game(user_number, rand=randint(1, 100)):
    for i in range(1, 10):
        if user_number == rand:
            print('Congratulations, you guessed it.')
            break
        if user_number > rand:
            print('Your number greater than.')
        if user_number < rand:
            print('Your number less than.')
        user_number = int(input(f'Try again. You have {10-i} more drinks left.\n'))
    else:
        print('You lost.')


def main():
    print('Welcome to the game of guess the numbers from 1 to 100 for 10 drinks.')
    game(int(input('Enter a number\n')))


if __name__ == '__main__':
    main()
