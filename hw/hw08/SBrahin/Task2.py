import re
password = input("Enter your password: ")

while True:

    if (len(password) < 6):
        print("Invalid Password. Please, input at least 6 symbols")
        break
    elif (len(password) > 16):
        print("Invalid Password. Please, input not more than 16")
        break
    elif not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        print("Invalid Password. Please, input at least 1 letter between [a-z] and 1 letter between [A-Z]")
        break
    elif not re.search("[0-9]", password):
        print("Invalid Password. Please, input at least 1 character from [0-9]")
        break
    elif not re.search("[$#@]" , password):
        print("Invalid Password. Please, input at least 1 character from [$#@]")
        break
    elif re.search("\s" , password):
        print("Invalid Password. Please, do not input spaces")
        break
    else:
        flag = 0
        print("Valid Password")
        break

#if flag == -1:
#    print("Not a Valid Password ")

