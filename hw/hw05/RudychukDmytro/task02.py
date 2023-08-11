
while True:
    user_input = input("Please enter a number: ")
    if user_input.isdigit():
        if int(user_input) == 0:
            print([0])
        elif int(user_input) == 1:
            print([0, 1])
        else: 
            f_numbers = [0, 1]
            n = int(user_input)
            for _ in range(n - 1):
                n = f_numbers[-1] + f_numbers[-2]
                f_numbers.append(n)
            print(f_numbers)
        question = input("Press 1 to continue or any other key to exit: ")
        if int(question) == 1:
            continue
        else:
            break

    else:
        print("Error, incorrect input!")

    

