import re

def password_validity(password):

    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$", password))

user_password = input("Please, enter your password: ")

if password_validity(user_password):
    print("Your password is correct!")

else:
    print("Invalid password. Please, try again.")