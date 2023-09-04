'''---------------Task_01-----------------'''

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

'''---------------Task_02-----------------'''

import math
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

'''---------------Task_03-----------------'''

def filter_words(st):
    words = st.split()
    formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(formatted_words)

'''---------------Task_04-----------------'''

def number_to_string(num):
    return f"{num}"

'''---------------Task_05-----------------'''

def reverse(st):
    return ' '.join(reversed(st.split()))

'''---------------Task_06-----------------'''

def reverse_list(l):
    return l[::-1]

'''---------------Task_07-----------------'''

def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

'''---------------Task_08-----------------'''

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left >= distance_to_pump / mpg

'''---------------Task_09-----------------'''

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"

'''---------------Task_10-----------------'''

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

'''---------------Task_11-----------------'''

def count_sheeps(sheep):
    return sheep.count(True)

'''---------------Task_12-----------------'''

def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False
