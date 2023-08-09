def main(login='First'):
    while True:
        log = input('Enter login: ')
        if log == login:
            print('Welcome')
            break
        else:
            print('Incorrect login. Please Try again.')


if __name__ == '__main__':
    main()
