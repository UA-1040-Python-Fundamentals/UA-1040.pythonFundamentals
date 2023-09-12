from random import random

def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

def main():
    #main cycle
    while True:
        rand_num = round(random() * 5)
        tries = 10
        print('Random number generated, you have 10 tries to guess')
        while tries:
            answer = int(input('Enter your answer: '))
            if answer == rand_num:
                print('You win!!!')
                break
            else:
                tries -= 1
                print('0 tries left, you loose') if tries == 0 else print(f'''You didn't guess, {tries} tries left''')

        if not continue_prgm_quest():
            print('Good bye.')
            break
        print('\n\r'*2)




if __name__ == "__main__":
    main()