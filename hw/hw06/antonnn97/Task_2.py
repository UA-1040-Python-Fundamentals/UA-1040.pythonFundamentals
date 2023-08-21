correct_login = "First"
user_login = input("Enter your login: ")

while user_login != correct_login:
    print("Error: Incorrect login.")
    user_login = input("Enter your login: ")

print(f"Hello, {user_login}!")