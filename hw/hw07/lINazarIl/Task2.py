import math

def rect():
    a = float(input('Please enter size of "A" side: '))
    b = float(input('Please enter size of "B" side: '))
    print('Area of rectagle: ', a * b)

def tria():
    a = float(input('Please enter size of "A" side: '))
    b = float(input('Please enter size of "B" side: '))
    c = float(input('Please enter size of "C" side: '))
    s = (a+b+c)/2
    print('Area of triangle: ', math.sqrt(s*(s-a)*(s-b)*(s-c)))

def circle():
    r = float(input('Please enter radius of circle: '))
    print('Area of circle: ', math.pi*r**2)

def continue_prgm_quest():
    choice = input('Continue program Y/N:')
    while not choice.lower() in ['y', 'n']:
        choice = input('Error, correct choice is Y or N: ')

    if choice.lower() == 'n':
        return False

    return True

def main():
    funcs = {1: rect, 2: tria, 3: circle}
    while True:
        func = int(input('Please select func: \n\r1)Rectangle\n\r2)Triangle\n\r3)Circle\n\r:'))
        if func < 4 and func > 0:
            funcs[func]()

        if not continue_prgm_quest():
            break
        print('\n\r'*2)


if __name__ == '__main__':
    main()