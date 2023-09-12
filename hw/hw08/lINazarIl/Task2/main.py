import re

def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

def validator(s):
    if not 6 <= len(s) <= 16:
        #print('Lenght not passed!!!')
        return False

    if not re.findall('[a-z]', s):
        #print('Small letters not passed!!!')
        return False

    if not re.findall('[A-Z]', s):
        #print('Capital letters not passed!!!')
        return False

    if not re.findall('[0-9]', s):
        #print('Numbers not passed!!!')
        return False

    if not re.findall('[$#@]', s):
        #print('Special symbols not passed!!!')
        return False

    return True

def main():
    while True:
        password = input('Please enter password for check: ')
        if validator(password):
            print('Your password correct')
        else:
            print('Your password not correct')

        if not continue_prgm_quest():
            break

        print('\n\r' * 2)

if __name__ == '__main__':
    main()
