import re

while True:
    password = input("Please, write me your password: ")
    az_check = re.findall("[a-z]+", password)
    AZ_check = re.findall("[A-Z]+", password)
    dollar_check = re.findall(r"\$", password)
    special_symbols_check = re.findall("#|@", password)
    numbers_check = re.findall("\d", password)

    if len(password) < 6:
        print("Please, input at least 6 symbols")
    elif len(password) > 16:
        print("Please, input not more than 16")
    elif len(az_check) < 1 or len(AZ_check) < 1:
        print("Please, input at least 1 letter between [a-z] and 1 letter between [A-Z]")
    elif len(dollar_check) < 1 and len(special_symbols_check) < 1:
        print("Please, input at least 1 character from [$#@]")
    elif len(numbers_check) < 1:
        print("Please, input at least 1 character from [0-9]")
    else:
        print("Thanks, now I know your password")
        break
1