# ----------------------------- Task 7.1 ---------------------
def largest_num(a, b):
    """This function returns the largest number of two numbers"""
    a = int(a)
    b = int(b)
    largest_num = max(a, b)
    return f"The largest number of two numbers is {largest_num}"


a = input("Enter your first number: ")
b = input("Enter your second number: ")
print(largest_num(a, b))

# ----------------------------- Task 7.2 ---------------------
print("--"*30)

from math import pi


def rectangle_area():
    """This function calculates the area of a rectangle"""
    a = int(input("Enter the length of the rectangle in centimeters: "))
    b = int(input("Enter the width of the rectangle in centimeters: "))
    area = int(a * b)
    return f"The area of the rectangle is {area} square centimeters."


def triangle_area():
    """This function calculates the area of a triangle"""
    a = int(input("Enter the base of the triangle in centimeters: "))
    b = int(input("Enter the height of the triangle in centimeters: "))
    area = int((a * b) / 2)
    return f"The area of the triangle is {area} square centimeters."


def circle_area():
    """This function calculates the area of a circle"""
    a = int(input("Enter the radius of the circle in centimeters: "))
    area = int(pi * a ** 2)
    return f"The area of the circle is {area} square centimeters."


while True:
    user_choice = input("""
    Please, choose the shape of a figure
    you want to calculate the area of:
    rectangle, triangle or circle?  """)
    user_choice = user_choice.lower()
    if user_choice == 'rectangle':
        print(rectangle_area())
        break
    elif user_choice == 'triangle':
        print(triangle_area())
        break
    elif user_choice == 'circle':
        print(circle_area())
        break
    else:
        print("Invalid shape. Please choose from rectangle, triangle or circle.")

# ----------------------------- Task 7.3 ---------------------
print("--"*30)


def count_char(word):
    """This function calculates the number of each character included in a string"""
    char_count = {}
    for char in word:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)


count_char(input("Enter your word: "))
