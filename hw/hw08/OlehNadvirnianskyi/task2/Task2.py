# Task 8.2
import re

user_password = str(input("Enter your password:"))
if len(user_password) >= 6 and len(user_password) <= 16 :
    check_azAZ = re.findall("[a-zA-Z]", user_password)
    if check_azAZ:
        check_09 = re.findall("[0-9]",user_password)
        if check_09:
            check_sumb = re.findall("[$#@]", user_password)
            if check_sumb:
                print('Welcome =)')
            else:
                print("Your password must contain the following characters: $#@")
        else:
            print("Your password must contain the following digits: 0-9")
    else:
        print("Your password must contain the letters: a-z A-Z")
else:
    print("Your password must be invalid! Сheck if it is between 6 and 16 characters")
