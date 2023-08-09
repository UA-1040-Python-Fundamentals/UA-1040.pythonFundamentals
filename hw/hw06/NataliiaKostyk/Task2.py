login = "First"

while True:
    user_input = input("Enter your login: ")
    if user_input == login:
        print(f"Hello, ", login + "!")
        break
    else:
        print("Invalid login. Please try again.")
