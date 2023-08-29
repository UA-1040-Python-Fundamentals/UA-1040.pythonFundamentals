def largest_num(num1, num2):
    """
    This function takes 2 numbers and find largest of them
    """
    return max([num1, num2])

def main():
    while True:
        num1 = int(input('Please enter number 1: '))
        num2 = int(input('Please enter number 2: '))
        print('Largest number is: ', largest_num(num1, num2))

        choice = input('Continue program Y/N:')
        while not choice.lower() in ['y', 'n']:
            choice = input('Error, correct choice is Y or N: ')

        if choice.lower() == 'n':
            break

        print('\n\r'*3, end='')

if __name__ == '__main__':
    main()