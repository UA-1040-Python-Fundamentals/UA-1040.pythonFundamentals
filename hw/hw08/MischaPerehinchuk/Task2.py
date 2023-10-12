import re

def check_password(password):

    if 6 <= len(password) <= 16:
        if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
            if re.search(r'[0-9]', password):
                if re.search(r'[$#@]', password):
                    return True
                else:
                    return False, "Пароль повинен містити принаймні 1 символ із [$#@]"
            else:
                return False, "Пароль повинен містити принаймні 1 число між [0-9]"
        else:
            return False, "Пароль повинен містити принаймні 1 літеру між [a–z] і 1 літеру між [A–Z]"
    else:
        return False, "Пароль повинен мати довжину від 6 до 16 символів"
password = input("Введіть пароль: ")

result = check_password(password)
if result is True:
    print("Пароль валідний!")
else:
    print("Пароль не валідний. Причина:", result[1])
