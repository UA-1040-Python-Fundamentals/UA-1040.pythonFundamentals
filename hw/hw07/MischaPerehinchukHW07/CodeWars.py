# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# II. Find The Distance Between Two Points
import math


def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    dist = round(dist, 2)
    return dist


# III. No yelling!
def filter_words(st):
    words = st.split()
    filtered_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    result = " ".join(filtered_words)
    return result


# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)


# V. Reversing Words in a String
def reverse(st):
    words = st.split()
    reversed = words[::-1]
    reversed_sentence = " ".join(reversed)
    return reversed_sentence


# VI.Reverse List Order
def reverse_list(l):
    return list(reversed(l))


# VII. Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    possible_distance = mpg * fuel_left
    if possible_distance >= distance_to_pump:
        return True
    else:
        return False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


# XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for is_present in sheep:
        if is_present:
            count += 1
    return count


# XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    else:
        return False


