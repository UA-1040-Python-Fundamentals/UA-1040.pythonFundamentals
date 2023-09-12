def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

class NegativeAge(Exception):
    pass

def main():
    while True:
        try:
            age = int(input('Enter age: '))
            if age < 0:
                raise NegativeAge

            if age % 2:
                print('Age odd')
            else:
                print('Age even')
        except NegativeAge:
            print('Entered age are negative')
        except ValueError:
            print('Incorrect input')

        if not continue_prgm_quest():
            print('Good bye.')
            break
        print('\n\r'*2)

if __name__ == '__main__':
    main()