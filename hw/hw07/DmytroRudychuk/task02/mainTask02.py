from functionTask02 import *


while True:
    menu = int(input("To calculate the area, choose: \n1 for rectangle \n2 for triangle \n3 for circle \nEnter: "))
    if menu == 1:
        s_rectangle()
    elif menu == 2:
        choice = int(input("If two sides and the angle between them are known, enter 1. \nIf three sides are known, enter 2 \n Enter: "))
        if choice == 1:
            s_triangle()
        elif choice == 2:
            s_triangle_geron()
        else: print("Error!")
    elif menu == 3:
        s_circle()
    else: print("Error!")
    if end_menu() is False:
        break