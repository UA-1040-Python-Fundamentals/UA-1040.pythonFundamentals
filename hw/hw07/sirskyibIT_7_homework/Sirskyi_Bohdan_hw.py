# # # # # # # 7     HomeWork

# Task 1

def largest_num(a, b):
    if a >= b:
        return a
    else:
        return b


a = input("Enter your first number: ")
b = input("Enter your second number: ")
print(f"The largest number between {a} and {b} is {largest_num(a, b)}")


# Task 2


choice = int(input("Choose your operation: 1 for rectangle, 2 for triangle and 3 for circle: "))

if choice == 1:
    def rectangle(a, b):
        return a * b
    length = float(input("Enter length your: "))
    width = float(input("Enter width your: "))
    area = rectangle(length, width)
    print(f"The area of the rectangle is: {area}")

elif choice == 2:
    def triangle(a, h):
        return 1 / 2 * a * h
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = triangle(base, height)
    print(f"The area of the triangle is: {area}")

elif choice == 3:
    def circle(r):
        return 3.14 * r * r
    radius = float(input("Enter radius: "))
    area = circle(radius)
    print(f"The area of the circle is: {area}")

else:
    print("Incorrect choice")



# Task 3


def count_characters(input_string):

    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


input_str = "Hola, amigo!"
char_count_result = count_characters(input_str)
print(char_count_result)
