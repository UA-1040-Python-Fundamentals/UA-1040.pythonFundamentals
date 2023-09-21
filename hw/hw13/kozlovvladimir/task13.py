# 1
names = ['Sam', 'Don', 'Daniel']


def hash_name(name):
    return hash(name)


hashed_names = list(map(hash_name, names))

print(hashed_names)

# 2
colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

red_items = list(filter(lambda x: x == "red", colors))

print(red_items)

# 3
# Using the append method:
str_numbers = ['1', '2', '3', '4', '5', '7']

int_numbers = []

for str_num in str_numbers:
    int_num = int(str_num)
    int_numbers.append(int_num)

print(int_numbers)

# Using the map method:
str_numbers = ['1', '2', '3', '4', '5', '7']

int_numbers = list(map(int, str_numbers))

print(int_numbers)

#4
miles_list = [1, 2, 3, 4, 5]

kilometers_list = list(map(lambda miles: miles * 1.6, miles_list))

print(kilometers_list)

#5
from functools import reduce

def find_max(x, y):
    return x if x > y else y

numbers = [12, 45, 78, 23, 56, 89, 34]

max_number = reduce(find_max, numbers)

print("The largest item in the list is:", max_number)

#6
def my_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

for num in my_range(1, 10, 2):
    print(num)

#7
def lettuce_decorator(sandwich_func):
    def add_lettuce():
        return "<\\ ^^^^^^^ />\n" + sandwich_func() + "\n<\\ ______ />"
    return add_lettuce

def tomato_decorator(sandwich_func):
    def add_tomato():
        return sandwich_func() + "\n# tomato #"
    return add_tomato

def meat_decorator(sandwich_func):
    def add_meat():
        return sandwich_func() + "\n- meat -"
    return add_meat

def salad_decorator(sandwich_func):
    def add_salad():
        return "~ salad ~"
    return add_salad

@lettuce_decorator
@tomato_decorator
@meat_decorator
@salad_decorator
def create_sandwich():
    return ""

print(create_sandwich())

