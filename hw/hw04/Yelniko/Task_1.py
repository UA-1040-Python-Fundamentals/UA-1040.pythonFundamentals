def fahrenheit(c):
    if c > -273.15:
        return (c*9/5)+32
    else:
        return 'Temperature is unacceptable'


if __name__ == '__main__':
    try:
        print(fahrenheit(float(input('Enter temperature\n'))))
    except ValueError:
        print('You didn\'t enter a number')


