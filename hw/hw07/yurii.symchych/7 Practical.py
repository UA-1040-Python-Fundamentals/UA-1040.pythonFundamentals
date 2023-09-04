#Task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#Task 2

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

#Task 3

def capitalized(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())


#Task 4

def number_to_string(number):
    return str(number)

#Task 5

def reverse(st):
    words = st.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

#Task 6
def reverse_list(l):
        return l[::-1]

#Task 7


#Task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
       fuel_nedeed = distance_to_pump / mpg
    return fuel_left >= fuel_nedeed

#Task 9

def are_you_playing_banjo(name):
 if name[0].lower() == 'r':
   return name + " plays banjo"
 else:
  return name + " does not play banjo"

#Task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#Task 11

def count_sheeps(sheep):
  return sheep.count(True)
  pass

#Task 12

def correct_tail(body, tail):
    return body[-1] == tail
