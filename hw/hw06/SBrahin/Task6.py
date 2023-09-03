# Завдання 1
testList = range(1,11)
for el in testList:
    if el % 2 == 0:
        print(f"{el} is divisible by 2")
    elif el % 3 == 0:
        print(f"{el} is divisible by 3")
    else:
        print(f"{el} are not divisible by 2 or 3")

# Завдання 2

userLogin = input("Input your login: ")
while userLogin == "First":
    print("Greetings, sir")
    break
else:
    print("Bad things happen :(")
