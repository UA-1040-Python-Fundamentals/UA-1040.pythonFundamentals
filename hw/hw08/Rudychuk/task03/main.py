from basic_logic import *


while True:
    menu = int(input("To calculate the area, choose: \n1 for rectangle \n2 for triangle \n3 for circle \nEnter: "))
    if menu == 1:
        s_rectangle()
    elif menu == 2:
        s_triangle()
    elif menu == 3:
        s_circle()
    else: print("Error!")
    if end_menu() is False:
        break