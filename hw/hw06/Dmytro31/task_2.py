
correct_login = "First"

user_login = input("Enter your login: ")

while user_login != correct_login:
    print("Error: Invalid login!")
    user_login = input("Enter your login: ")

print("Hello, {}!".format(user_login))