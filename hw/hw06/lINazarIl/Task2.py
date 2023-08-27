allowed_login = 'First'
while True:
    login = input('Please enter login: ')
    if login == allowed_login:
        print('Greetings, you are logged')
        break
    print('Error, your login is not allowed')