#Task2. Write a script that checks the login that the user enters.
#If the login is "First", then greet the users. If the login is
#different, send an error message.
#(need to use loop while)


# Initialize a variable to store the user's input
login = input("Enter your login: ")

# Use a while loop to keep asking for the login until it's "First"
while login != "First":
    print("Error: Incorrect login.")
    login = input("Enter your login again: ")

# When the loop exits, it means the user entered "First"
print("Hello, user!")