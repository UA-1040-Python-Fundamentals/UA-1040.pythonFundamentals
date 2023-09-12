import re

def validity_of_password(password):
    length_regex = re.compile(r'^.{6,16}$')
    lowercase_regex = re.compile(r'[a-z]')
    uppercase_regex = re.compile(r'[A-Z]')
    digit_regex = re.compile(r'[0-9]')
    special_char_regex = re.compile(r'[$#@]')

    if (length_regex.search(password) and
        lowercase_regex.search(password) and
        uppercase_regex.search(password) and
        digit_regex.search(password) and
        special_char_regex.search(password)):
        return True
    else:
        return False


password = input("Enter a password: ")


if validity_of_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")