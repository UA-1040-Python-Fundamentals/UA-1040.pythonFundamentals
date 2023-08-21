print("Login must be \"First\"")
print("You have only 3 tries\n")
i = 0
while i < 3:
    i += 1
    login = input(f"Try #{i}. Enter the login: ")
    if login == "First" or login == "first":
        print("Hello User!")
        break
    else:
        print("Error!")
        if i < 3:
            print("Try again!\n")
        else:
            print("You have 0 tries")


# for i in range(3):
#     i += 1
#     login = input(f"Try #{i}. Enter the login: ")
#     if login == "First" or login == "first":
#         print("Hello User!")
#         break
#     else:
#         print("Error!")
#         if i < 3:
#             print("Try again!\n")
#         else:
#             print("You have 0 tries")
#         continue

