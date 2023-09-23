# This script checks user login and provides appropriate messages using a while loop.
# Infinite loop until the correct login is entered
# Write a script that checks the login that the use enters
# If the login is "First" then greet the users.
# If the login is different, send an error message.
# (need to use loop while)
while True:
    login = input("Enter your login: ")

    if login == "First":
        print("Hello, welcome!")
        break  # Exit the loop if login is "First"
    else:
        print("Error: Incorrect login. Please try again.")