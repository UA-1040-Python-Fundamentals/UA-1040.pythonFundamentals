import re

def digit(word):
    for i in range(len(word)):
        if word[i].isdigit():
            return True


def title(word):
    for i in range(len(word)):
        if word[i].istitle():
            return True


print("Choose your password")

password = input()

if 6 <= len(password) <= 16:
    if password.find('#') or password.find('$') or password.find('@'):
        if digit(password):
            if re.search(r'/d', password):
                if title(password):
                    print("Your password is completely correct")
                else:
                    print("password must contain title letters")
            else:
                print("password must contain letters")
        else:
            print("password ,ust contain digits")
    else:
        print("Password must contain special symbols")

else:
    print("incorrect length")