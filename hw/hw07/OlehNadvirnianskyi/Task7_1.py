# Task1
# Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function)
def largest(num1, num2):
    '''
    Function take two numbers and return the largest number.
    '''
    d = [num1,num2]
    return max(d)

print(largest(23,6))


# Task3. Write a function that calculates the number of characters
# • input: "hello"
def calcul(word):
    '''
    Function return the number of characters in a given string
    '''
    all_d= {}
    for x in str(word):
        all_d.update({f"{x}": word.count(x)})
    return all_d
# • output: {"h":1, "e":1,"l":2,"o":1}

print(calcul("hello"))



# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
# included in a given string

from math import pi
def rectangle(length, width):
    ''' Function calculates the area of a rectangle '''
    s_rectangle = int(length) * int(width)
    return s_rectangle


def triangle(heigh, base):
    ''' Function calculates the area of a triangle '''
    s_triangle = int(heigh)*int(base)/2
    return s_triangle
def circle(radius):
    ''' Function calculates the area of a circle '''
    s_circle = pi*(int(radius)**2)
    return s_circle

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




