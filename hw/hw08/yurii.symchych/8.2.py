def is_valid_password(password):
    if 6 <= len(password) <= 16:
        if any(c.islower() for c in password):
            if any(c.isupper() for c in password):
                if any(c.isdigit() for c in password):
                    if any(c in '$#@' for c in password):
                        return True

    return False


password = input("Enter password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")