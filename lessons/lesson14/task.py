import re
from random import choices
from string import ascii_letters, digits


def check(login):
    if not re.match(r"^(admin|employee)(-|id|-id)?(\d*$)", login, re.I):
        raise ValueError(f"incorrect login '{login}'")
    return True


letters_and_digits = choices(ascii_letters, k=5)
letters_and_digits.extend(choices(digits, k=5))
incorect_login = ''.join(letters_and_digits)
try:
    if check(incorect_login):
        print("checked successfully")
except ValueError as e:
    print(str(e) == f"incorrect login '{incorect_login}'")
