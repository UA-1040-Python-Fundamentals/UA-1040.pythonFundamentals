#-------------------------------- Task 7.2.1 (Jenny's secret message) ---------------------------------------
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

print(greet('Karl'))
print(greet('Johnny'))

#------------------------- Task 7.2.2 (Find The Distance Between Two Points) --------------------------------
def distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 2)

print(distance(1,1,0,0)) #1.41

#--------------------------------------- Task 7.2.3 (No yelling!) -------------------------------------------

def filter_words(st):
    normal_text = " ".join((st.capitalize()).split())
    return normal_text

print(filter_words("heLLo! iT'S       mE!"))

#-------------------------------- Task 7.2.4 (Convert a Number to a String) ---------------------------------

def number_to_string(num):
    return str(num)

print(number_to_string(4213))

#-------------------------------- Task 7.2.5 (Reversing Words in a String) ----------------------------------

def reverse(st):
    words = st.strip().split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

print(reverse("Hello world"))

#------------------------------------- Task 7.2.6 (Reverse List Order) --------------------------------------

def reverse_list(l):
  return l[::-1]

print(reverse_list([1,2,3,4,5]))

#------------------------------------- Task 7.2.7 (Multiples of 3 or 5) -------------------------------------

def solution(number):
    list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
    return sum(list)

print(solution(6))

#------------------------------------- Task 7.2.8 (Will you make it?) ---------------------------------------

def zero_fuel(distance_to_pump, mpg, fuel_left):
    miles_possible = mpg * fuel_left
    return miles_possible >= distance_to_pump

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))

#----------------------------------- Task 7.2.9 (Are You Playing Banjo?) ------------------------------------

def are_you_playing_banjo(name):
    # Implement me!
    if name.lower()[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo("Richard"))
print(are_you_playing_banjo("Alexander"))

#--------------------- Task 7.2.10 (Convert boolean values to strings 'Yes' or 'No’) ------------------------

def bool_to_word(boolean=True):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"

print(bool_to_word())
print(bool_to_word(False))

#----------------------------------- Task 7.2.11 (Counting sheep) -------------------------------------------

def count_sheeps(sheep):
    sheeps = 0
    for i in sheep:
        if i == True:
            sheeps += 1
        else:
            pass
    return sheeps

print(count_sheeps ([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))

#----------------------------------- Task 7.2.12 (Is this my tail?) -----------------------------------------

def correct_tail(body, tail):
    if body[-1:] == tail:
        return True
    else:
        return False
    
print(correct_tail("Fox", "x"))
print(correct_tail("Lion", "b"))
