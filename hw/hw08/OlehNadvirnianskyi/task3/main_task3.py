from functions_task3 import *

user_pick = input('''Choose a figure:
1.Rectangle
2.Triangle
3.Circle
Pick one:''')

if user_pick == "1":
    length= input("Enter length of rectangle:")
    width= input("Enter width of rectangle:")
    print(f"{rectangle(length,width)} cm2")
elif user_pick == "2":
    heigh = input("Enter heigh of triangle:")
    base = input("Enter base of triangle:")
    print(f"{(triangle(heigh,base))} cm2")

elif user_pick == "3":
    radius = input("Enter radius of circle:")
    print(f"{circle(radius)} cm2")
