def fibonacci(num_user, num_1=0, num_2=1):
    print(num_1)
    for i in range(1, num_user):
        print(num_2)
        num_1, num_2 = num_2, num_2 + num_1


def main():
    try:
        fibonacci(num_user=int(input('Enter number ')))
    except ValueError:
        print('You didn\'t enter a number')


if __name__ == '__main__':
    main()
