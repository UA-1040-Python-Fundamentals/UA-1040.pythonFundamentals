def rectangle(lis: list):
    lis = list(map(int, lis))
    return f'S = {lis[0] * lis[1]}'


def triangle(lis: list):
    lis = list(map(int, lis))
    return f'S = {0.5 * lis[0] * lis[1]}'


def circle(r: int, pi=3.14):
    return f'S = {pi * (r ** 2)}'


def mein():
    print('[OK] Program successfully started\n')
    while True:
        try:
            num = int(input('Enter 1 to calculate the area of the rectangle.\n'
                            'Enter 2 to calculate the area of the triangle.\n'
                            'Enter 3 to calculate the area of the circle.\n'
                            'Enter 4 to exit\n'
                            'Enter: '))
            if num == 1:
                print(rectangle(input('Enter the two sides of the rectangle using commas.\n'
                                      'Enter: ').split(',')))
            if num == 2:
                print(triangle(list(input('State the sides and altitudes of the triangle using commas.\n'
                                          'Enter: ').split(','))))
            if num == 3:
                print(circle(int(input('Enter the radius of the circle.\n'
                                       'Enter: '))))
            if num == 4:
                break
        except ValueError:
            print('[No] An erroneous value has been entered\n')


if __name__ == '__main__':
    mein()
    print('[OK] Program successfully completed ')
