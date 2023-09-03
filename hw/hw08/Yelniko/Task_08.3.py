from math import pi


def area(key, lis):
    match key:
        case 'RECTANGLE':
            return lis[0] * lis[1]
        case 'TRIANGLE':
            return 0.5 * lis[0] * lis[1]
        case 'CIRCLE':
            return pi * lis[0] ** 2


def main():
    while True:
        key = input('Enter the name of the form\nRECTANGLE, TRIANGLE, CIRCLE\nTo exit, enter exit\n')
        key = key.upper()
        if key == 'RECTANGLE':
            print(area(key, list(map(int, input('Enter 2 sides separated by a comma\n').split(',')))))
        if key == 'TRIANGLE':
            print(area(key, list(map(int, input('Enter the altitude then the '
                                                'side separated by a comma.\n').split(',')))))
        if key == 'CIRCLE':
            print(area(key, list(map(int, input('Enter radius\n')))))
        if key == 'EXIT':
            break


if __name__ == '__main__':
    main()
