#------------------------ Task 8.1 ------------------------

def correct_pass():
    import re
    import string

    alph_low = "|".join(string.ascii_lowercase)
    alph_up = "|".join(string.ascii_uppercase)

    while True:
        Username = input("Enter the Username: ")
        Password = input("Enter the password: ")

        match_lower = re.findall(alph_low, Password)
        match_upper = re.findall(alph_up, Password)
        match_char = re.findall("@|#|$", Password)

        if len(Password) > 6 and len(Password) < 16:
            if len(match_lower) > 0:
                print("Lowercase match found. Checking for uppercase...")
                if len(match_upper) > 0:
                    print("Uppercase match found. Checking for character @ or # or $ ...")
                    if len(match_char) > 1: # На 16 стрічці проблема з імпортованим модулем який не розпізнає символ "$" та ставить '' у print()
                        print("Your password is good!")
                        break
                    else:
                        print("No special characters found")
                        continue
                else:
                    print("No found uppercase match")
                    continue
            else:
                print("No found lowercase")
                continue
        else:
            print("Your password must be larger than 6 and less than 16 characters long")
            continue

correct_pass()

#------------------------ Task 8.2 ------------------------

from math import pi, pow

def rectangle_ar():
    """This function calculates the area of a rectangle"""
    a = int(input("Enter the 'a' side length in centimeters: "))
    b = int(input("Enter the 'b' side length in centimeters: "))
    area = a+b
    return (f"Area of a rectangle - {area} square centimeters")

def triangle_ar():
    """This function calculates the area of a triangle"""
    a = int(input("Enter the 'a' side length in centimeters: "))
    h = int(input("Enter the height value 'h' in centimeters: "))
    area = (a*h)/2
    return (f"Area of a triangle - {area} square centimeters")

def circle_ar():
    """This function calculates the area of a circle"""
    r = float(input("Enter the radius length in centimeters: "))
    area = round(pi * pow(r, 2), 2) # Using the imported pow() and pi functions
    return (f"Area of a circle - {area} square centimeters")

#-------------------- "Module import simulation" ------------------

#from Task_8 import rectangle_ar, triangle_ar, circle_ar---

while True:
    choice = input("""
    What exactly do you want to calculate the area of: 
1. Rectangle
2. Triangle
3. Сircle? 
    To choose, write the number or press the Enter to exit:  """)
    if choice == "":
        print("Exiting...")
        break

    try:
        choice_int = int(choice)
        if choice_int == 1:
            print(rectangle_ar()) #Imported from Task_8
        elif choice_int == 2:
            print(triangle_ar()) #Imported from Task_8
        elif choice_int == 3:
            print(circle_ar()) #Imported from Task_8
        else:
            print("\nSelect an existing variant.")
    except ValueError:
        print("Enter the correct value")