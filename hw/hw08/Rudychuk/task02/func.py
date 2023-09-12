import re

def check_password_validity(password):
    if 6 <= len(password) <= 16:
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            if re.search("[0-9]", password):
                if re.search("[$#@]", password):
                    return "Valid password"
                else:
                    return "Password must contain at least one of the characters [$#@]"
            else:
                return "Password must contain at least one digit [0-9]"
        else:
            return "Password must contain at least one lowercase letter [a-z] and one uppercase letter [A-Z]"
    else:
        return "Password length should be between 6 and 16 characters"