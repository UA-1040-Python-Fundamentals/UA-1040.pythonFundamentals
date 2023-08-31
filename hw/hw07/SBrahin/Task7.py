#Task 1

def maxAmount(num1 : int,num2 : int):
    """This function returns the largest number of two numbers"""
    if num1 < num2:
        return num2
    else:
        return num1

user_input = int(input("Please, enter your first number:"))
user_input_second = int(input("Please, enter your second number:"))
total = maxAmount( user_input, user_input_second )
print(f"The largest number - {total}")

#Task2

def rectangle(length: int, width: int ):
    """This function calculates the area of a rectangle"""
    area = length * width
    return area

def triangle(base : int, perpendecularHeight : int ):
    """This function calculates the area of a triangle"""
    area = 1/2 * base * perpendecularHeight
    return area

def circle(radius , pi = 3.14):
    """This function calculates the area of a circle"""
    area = pi * radius**2
    return round(area, 2)

user_input = input("Hello, what do you want to calculate?"
                   "\n Area of a rectangle = 1"
                   "\n Area of a triangle = 2"
                   "\n Area of a circle = 3"
                   "\n Input the number here: ")

if user_input == '1':
    data_lenght = int(input("Please, input lenght: "))
    data_width = int(input("Please, input width: "))
    total = rectangle(data_lenght,data_width)
    print(f"The area of a rectangle is - {total}")
elif user_input == '2':
    data_base = int(input("Please, input base: "))
    data_perpendecularHeight = int(input("Please, input perpendecular height: "))
    total = triangle(data_base, data_perpendecularHeight)
    print(f"The area of a triangle is - {total}")
elif user_input == '3':
    data_radius = int(input("Please, input radius: "))
    total = circle(data_radius)
    print(f"The area of a circle is - {total}")
else:
    print("Invalid input!")

#Task 3

def wordCounter(word):
    """This function calculates the area of a rectangle"""
    dict = {}
    for x in word:
        counter = word.count(x)
        dict[x] = counter
    return (dict)

user_input = str(input("Please, enter your word:"))

print(wordCounter(user_input))
