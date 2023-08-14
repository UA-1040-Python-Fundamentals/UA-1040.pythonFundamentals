#  ----------------------------- Task 01 ---------------------
def greet(name):
    """This function returns a greeting for a user. However, Jenny's in love with Johnny
    and would like to greet him slightly different. We added a special case to her greetings"""
    if name == "Jonny":
        return "I love you Jonny!"
    else:
        return f"Hello {name}!"


name = input("What is your name? ")
print(greet(name))

#  ----------------------------- Task 02 ---------------------


def distance(x1, y1, x2, y2):
    """This function  calculates the distance between two ordered pairs,
    and we rounded them to two decimal places"""
    return round((((x2-x1)**2)+((y2-y1)**2))**0.5, 2)


print(distance(3, 5, -2, 7))

#  ----------------------------- Task 03 ---------------------


def filter_words(s):
    """This function returns capitalized and properly spaced strings"""
    return ' '.join(s.capitalize().split())


print(filter_words("WOW this is REALLY          amazing!"))
print(filter_words('HELLO CAN YOU HEAR ME?'))

#  ----------------------------- Task 04 ---------------------


def number_to_string(num):
    """These functions transform a number (integer) into a string"""
    return repr(num)


print(number_to_string(45), type(number_to_string(45)))


def number_to_string(num):
    return str(num)


print(number_to_string(-100), type(number_to_string(-100)))


#  ----------------------------- Task 05 ---------------------


def reverse_words(s):
    """This function reverses the words in a given string"""
    return ' '.join(reversed(s.split()))


print(reverse_words("Hi there! How are you?"))

#  ----------------------------- Task 06 ---------------------


def reversed_list(lst):
    """This function takes in a list and returns a list with the reverse order"""
    return lst[::-1]


print(reversed_list([1, 2, 3, 4]))

#  ----------------------------- Task 07 ---------------------


def solution(num):
    """This function returns the sum of all the multiples of 3 or 5 below the number passed in.
    If the number is negative, it returns 0. If the number is a multiple of both 3 and 5,
    it only counts it once"""
    if num < 0:
        return 0
    multiples = [i for i in range(num) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples)


print(solution(20))
print(solution(55))

#  ----------------------------- Task 08 ---------------------


def can_reach_pump(distance, mpg, fuel_left):
    """This function tells you if it is possible to get to the pump or not"""
    max_distance = mpg * fuel_left
    if max_distance >= distance:
        return True
    else:
        return False


print(can_reach_pump(50, 25, 2))
print(can_reach_pump(30, 25, 1))

#  ----------------------------- Task 09 ---------------------


def is_playing(name):
    """This function takes a name as its only argument and if it starts with 'R' or 'r',
    it returns name + plays banjo, otherwise name + does not play banjo"""

    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo."
    else:
        return f"{name} does not play banjo."


name = input("Do you play banjo? Enter your name to find out: ")
print(is_playing(name))

#  ----------------------------- Task 10 ---------------------


def bool_to_str(boolean):
    """This function takes a boolean value and return a "Yes" string for true,
    or a "No" string for false"""
    if type(boolean) == bool:
        if boolean is True:
            return "Yes"
        else:
            return "No"


print(bool_to_str(True))
print(bool_to_str(False))

#  ----------------------------- Task 11 ---------------------


def count_sheep(sheep):
    """This function counts the number of sheep present in the array"""
    count = 0
    for i in sheep:
        if type(i) == bool:
            if i is True:
                count += 1
    return count


print(count_sheep([True, True, True, False,
                  True,  True,  True,  True,
                  True,  False, True,  False,
                  True,  False, False, True,
                  True,  True,  True,  True,
                  False, False, True,  True]))

#  ----------------------------- Task 12 ---------------------


def correct_tail(body, tail):
    """This function checks if the second argument (tail) is the same as the last letter
    of the first argument (body) and if the tail is right returns True, else returns False"""
    if body.endswith(tail):
        return True
    else:
        return False


print(correct_tail("Fox", "x"))
print(correct_tail("Giraffe", "d"))
