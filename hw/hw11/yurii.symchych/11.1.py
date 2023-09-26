try:
    user_input = int(input("Enter an integer: "))
    if user_input % 2 == 0:
        print(f"{user_input} is an even number.")
    else:
        print(f"{user_input} is an odd number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
