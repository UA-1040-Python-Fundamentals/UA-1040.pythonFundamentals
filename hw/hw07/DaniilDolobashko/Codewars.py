#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#2
def distance(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(distance, 2)

#3
def filter_words(st):
    words = st.split()
    words[0] = words[0].capitalize()
    for i in range(1, len(words)):
        words[i] = words[i].lower()
    filtered_st = ' '.join(words)
    return filtered_st

#4
def number_to_string(num):
    return str(num)

#5
def reverse(st):
    st_split = st.split()
    reversed_list = list(reversed(st_split))
    reversed_string = ' '.join(reversed_list)
    return reversed_string

#6
def reverse_list(l):
    return l[::-1]

#7
def solution(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
        if i % 3 == 0 and i % 5 == 0:
            sum -= i
    return sum

#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel_distance = mpg * fuel_left
    if distance_to_pump > fuel_distance:
        return False
    return True

#9
def are_you_playing_banjo(name):
    name_split = name.split()
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

#10
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    return "No"

#11
def count_sheeps(sheep):
    counter = 0
    for i in range(0, len(sheep)):
        if sheep[i] == True:
            counter += 1
    return counter

#12
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False