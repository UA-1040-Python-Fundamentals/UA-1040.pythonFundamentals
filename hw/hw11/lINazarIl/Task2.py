import calendar

def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

days_of_week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednessday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

def main():
    while True:
        try:
            num = int(input('Please enter number: '))
            print(days_of_week[num])

        except ValueError:
            print('Incorrect value')

        except KeyError:
            print('Num out of range')


        if not continue_prgm_quest():
            print('Good bye.')
            break
        print('\n\r'*2)

if __name__ == '__main__':
    main()