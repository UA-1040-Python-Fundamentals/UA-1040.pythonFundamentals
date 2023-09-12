from module import  *

def continue_prgm_quest():
    choice = input('Continue program Y/N: ')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

def main():
    while(True):
        print('Please select function\n\r1.Rectangle\n\r2.Triangle\n\r3.Circle\n\r:', end=' ')
        sf = int(input())
        match sf:
            case 1:
                A = int(input('Please enter "A" side: '))
                B = int(input('Please enter "B" side: '))
                S = rect(A, B)
                print(f'Area of rectagle: {S}')

            case 2:
                H = int(input('Please enter height of triangle: '))
                A = int(input('Please enter base of triangle: '))
                S = triac(H, A)
                print(f'Area of triangle: {S}')
            case 3:
                R = int(input('Please enter radius of the circle: '))
                S = circle(R)
                print(f'Area of the circle: {S}')
            case _:
                print('Invalid function!!!')

        if not continue_prgm_quest():
            break

        print('\n\r'*2)


if __name__ == "__main__":
    main()
