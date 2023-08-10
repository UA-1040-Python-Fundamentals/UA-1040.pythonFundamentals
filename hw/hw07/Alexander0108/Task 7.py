#-------------------------------- Task 7.1 ---------------------------------------
def largest_long_numb(*numbers):
    """This function return the largest(longest) number of numbers"""
    numbers = []
    largest_num = 0
    len_list = [0]

    while True:
        number = input("Enter your numbers (or press Enter to finish): ")

        if number == "":
            break

        try:
            number1 = float(number)
            numbers.append(number1)
        except ValueError:
            print("Invalid input. Please enter a valid number")

    for i in numbers:
        len_num = len(str(i))
        if len_num > max(len_list):
            largest_num = i
        len_list.append(len_num)

    return (f"The largest(longest) numb is: {largest_num}")

print(largest_long_numb())

print("--"*10)
print("The next function")


def largest_big_numb(*numbers):
    """This function return the largest(biggest) number of numbers"""
    numbers = []
    while True:
        number = input("Enter your numbers (or press Enter to finish): ")

        if number == "":
            break

        try:
            number1 = float(number)
            numbers.append(number1)
        except ValueError:
            print("Invalid input. Please enter a valid number")
    
    return (f"The largest number is: {max(numbers)}")

print(largest_big_numb())

#-------------------------------- Task 7.2 ---------------------------------------

print("--"*30)
from math import pi

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
    area = round(pi * (r**2), 2)
    return (f"Area of a circle - {area} square centimeters")

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
            print(rectangle_ar())
        elif choice_int == 2:
            print(triangle_ar())
        elif choice_int == 3:
            print(circle_ar())
        else:
            print("\nSelect an existing variant.")
    except ValueError:
        print("Enter the correct value")


#-------------------------------- Task 7.3 ---------------------------------------

print("--"*30)
def count_letters(word):
    """This function counts the number of letters in a word"""
    symbols = {}
    count = 1
    for i in word:
        if i not in symbols:
            count = 1
            symbols.update({i: count})
        elif i in symbols:
            count += 1
            symbols.update({i: count})
    print(symbols)

count_letters("Hellllloooo")