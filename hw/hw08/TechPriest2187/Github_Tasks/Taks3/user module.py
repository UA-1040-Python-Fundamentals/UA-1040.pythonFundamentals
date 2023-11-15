from admin_module import *

print("what area do you want to get?")

answer = input()

if answer == "rectangle":
    print(rect(int(input()),int(input())))

elif answer == "triangle":
    print(triangle(int(input()),int(input())))

else:
    print(circle(int(input())))