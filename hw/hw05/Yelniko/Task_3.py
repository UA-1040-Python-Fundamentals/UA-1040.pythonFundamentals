def fibonacci(num_user):
    num = 1
    for i in range(1, num_user+1):
        num *= i
    return num


def main():
    try:
        print(fibonacci(num_user=int(input('Enter number '))))
    except ValueError:
        print('You didn\'t enter a number')


if __name__ == '__main__':
    main()
