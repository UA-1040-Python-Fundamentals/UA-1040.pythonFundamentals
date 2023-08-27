#task7.1
def return_largest_number(number_one, number_two):
    """Returns the largest number of two given numbers."""
    if number_one > number_two:
        return number_one
    elif number_one < number_two:
        return number_two
print(return_largest_number(10, 8))

#task7.2
def calculates_the_area_of_a_rectangle(x, y):
    return x * y
def calculates_the_area_of_a_triangle(x, y):
        return 1 / 2 * x * y
def calculates_the_area_of_a_circle(x):
        return 3.14 * x ** 2
a = int(input('1 for rectangle, 2 for triangle, 3 for circle: '))
if a == 1:
    l = float(input("length: "))
    w = float(input("width: "))
    ar = calculates_the_area_of_a_rectangle(l, w)
    print(f"The area of the rectangle is: {ar}")
elif a == 2:
    b = float(input("length: "))
    h = float(input("height: "))
    ar = calculates_the_area_of_a_triangle(b, h)
    print(f"The area of the triangle is: {ar}")
elif a == 3:
    r = float(input("radius: "))
    ar = calculates_the_area_of_a_circle(r)
    print(f"The area of the circle is: {ar}")
else:
    print("Invalid choice")


#task7.3
my_string = 'hello'
def return_largest_number(my_string):
    dict_sample = {}
    for x in range(len(my_string)):
        if my_string[x] in dict_sample:
            continue
        else:
            y=my_string[x]
            z=my_string.count(y)
            dict_sample[y] = z
    return dict_sample
print(return_largest_number(my_string))