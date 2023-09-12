def char_count(str):
    counted = {}
    for i in str:
        if i in counted:
            counted[i] += 1
            continue

        counted[i] = 1

    return counted

def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

def main():
    while True:
        str = input('Please enter sentence: ')
        counted = char_count(str)
        for i in counted:
            print(f'Character {i} was found: {counted[i]} times')

        if not continue_prgm_quest():
            break

        print('\n\r'*2)


if __name__  == '__main__':
    main()