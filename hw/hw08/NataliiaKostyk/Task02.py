def check_password(password):
    import re
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$"
    regex = re.compile(pattern)
    match = regex.match(password)
    return bool(match)


password = input("Please, enter the password: ")
if check_password(password):
    print("The password is valid.")
else:
    print("The password is invalid.")
