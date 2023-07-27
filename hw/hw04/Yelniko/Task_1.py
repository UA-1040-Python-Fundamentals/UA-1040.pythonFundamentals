def fahrenheit(c):
    if c > -273.15:
        return f'{c}`C is equivalent to {(c*9/5)+32}`F'
    else:
        return 'Error: Temperature below absolute zero(-273.15`C)'


if __name__ == '__main__':
    try:
        print(fahrenheit(float(input('Enter the temperature in Celsius: '))))
    except ValueError:
        print('You didn\'t enter a number')


