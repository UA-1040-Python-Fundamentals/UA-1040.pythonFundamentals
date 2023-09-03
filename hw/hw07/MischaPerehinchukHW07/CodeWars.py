# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
# II. Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    dist =math.sqrt((x2-x1) ** 2 +(y2-y1) ** 2)
    dist = round(dist,2)
    return dist
# III. No yelling!
def filter_words(st):
    words = st.split()
    filtered_words = [words[0].capitalize()] +[word.lower() for word in words[1:]]
    result = " ".join(filtered_words)
    return result
# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)
# V. Reversing Words in a String

def reverse(st):
    words =st.split()
    reversed = words[::-1]
    reversed_sentence = " ".join(reversed)
    return reversed_sentence
# VI.Reverse List Order