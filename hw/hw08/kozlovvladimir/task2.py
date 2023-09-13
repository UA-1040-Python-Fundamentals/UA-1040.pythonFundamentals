import re

password = str(input("input from users:"))

def validity_of_a_password(password):
    answer= False

    if  6 <= len(password) <= 16 and re.findall('[a-z]', password) and re.findall('[A-Z]', password) and re.findall('[0-9]', password) and re.findall('[$#@]', password):
        answer=True

    return answer

print(validity_of_a_password(password))

