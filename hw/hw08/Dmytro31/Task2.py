import re

def is_valid_password(password):
    if 6 <= len(password) <= 16:
        if re.search(r'[a-z]', password):
            if re.search(r'[A-Z]', password):
                if re.search(r'[0-9]', password):
                    if re.search(r'[$#@]', password):
                        return True

    return False

password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")