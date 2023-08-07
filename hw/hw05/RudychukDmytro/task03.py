
while True:
    user_input = input("Please enter a number: ")
    if user_input.isdigit():
        num = int(user_input)
        factorial = 1
        while num > 0:
            factorial *= num
            num -= 1
        print(f"Factorial of the number {num} will be the value {factorial}.")
        question = input("Press 1 to continue or any other key to exit: ")
        if int(question) == 1:
            continue
        else:
            break

    else:
        print("Error, incorrect input!")