# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)


login = {'name': 'First'}
while True:
    user_input = input('Please input the login: ')
    if user_input == login['name']:
        print('Login successful')
        break
    else:
        print('Login failed. Please try again')

