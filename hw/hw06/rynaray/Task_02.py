valid_login = "First"
user_input = input("Enter your login: ")

while user_input != valid_login:
    print("Error: Incorrect login. Please try again.")
    user_input = input("Enter your login: ")

print("Welcome, " + user_input + "!")