import re


def verification(password):
    return [
        sum(1 for i in password if i.islower()) > 0,
        sum(1 for i in password if i.isupper()) > 0,
        len(re.findall('[0-9]', password)) > 0,
        len(re.findall('[$#@]', password)) > 0,
        len(password)
    ]


def main():
    while True:
        ver = verification(input('Enter your password\n'))
        if not ver[0]:
            print('The password must contain letters.')
        elif not ver[1]:
            print('The password must have one capital letter.')
        elif not ver[2]:
            print('The password must contain the digits.')
        elif not ver[3]:
            print('The password must contain a special character (@, $, #).')
        elif not 6 < ver[4] < 16:
            print('The password must be between 6 and 16 characters')
        else:
            print('Your password is correct.')
            break


if __name__ == '__main__':
    main()
