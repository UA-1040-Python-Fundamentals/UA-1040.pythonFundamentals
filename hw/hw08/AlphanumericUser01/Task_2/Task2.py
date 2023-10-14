# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

user_input = input("Please enter your password: ")


def letters_check(user_input):
    f"""This function checks the occurrence of letters [a-z] in the entered password """
    match = re.search(r"[a-zA-Z0-9$#@]", user_input)
    if match:
        if 6 <= len(user_input) <= 16:
            return "The password is valid"
        else:
            return "The password length is not valid. It should be between 6 and 16 characters."
    else:
        return ("The password is not valid\n"
                "It should have at least 1 letter between [a-z] and 1 letter between [A-Z];\n"
                "At least 1 number between [0-9];\n"
                "At least 1 character from [$#@]")


a = letters_check(user_input)
print(a)
