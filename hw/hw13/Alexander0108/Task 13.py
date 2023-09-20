#------------------------------------ Task 13.1 -----------------------------------------

names = ['Sam', 'Don', 'Daniel'] 
print(names)
names = map(lambda x: hash(x), names)
print(list(names))

#------------------------------------ Task 13.2 -----------------------------------------

lst = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
lst_wo_red = filter(lambda n: n != "red", lst)
print(list(lst_wo_red))

#------------------------------------ Task 13.3 -----------------------------------------

str_numb = ['1','2','3','4','5','6','7']

#Using the append method
int_numb = []

for str_num in str_numb:
    int_num = int(str_num)
    int_numb.append(int_num)

print(int_numb)

#Using the map method
int_numb = list(map(lambda x: int(x), str_numb))
print(int_numb)

#------------------------------------ Task 13.4 -----------------------------------------

miles = [1,2,3,4,5]

#Using the map and some function

def convert(miles):
    return round((miles * 1.6), 3)

kilometers = list(map(convert,miles))
print(kilometers)

#Using the map and lambda function

kilometers = list(map(lambda x: round((x*1.6),3), miles))
print(kilometers)

#------------------------------------ Task 13.5 -----------------------------------------
from functools import reduce

lst = [1,2,7,4,2,665,234]

def find_max(x, y):
    return x if x > y else y

print(f"Larges item in the list is: {reduce(find_max, lst)}")

#------------------------------------ Task 13.6 -----------------------------------------

def iter(start, stop, step=1):
    current = start
    while current < stop if step>0 else current > stop:
        yield current
        current += step

for num in iter(1,20,8):
    print(num)

#------------------------------------ Task 13.7 -----------------------------------------

def bread(func):
    def wrapper():
        print("<\ ^^^^^^^ />")
        func()
        print("<\ ______ />")
    return wrapper

def lettuce(func):
    def wrapper():
        print("~ lettuce ~")
        func()
    return wrapper

def tomatoes(func):
    def wrapper():
        print("# tomato #")
        func()
    return wrapper

def meat(func):
    def wrapper():
        print("- meat -")
        func()
    return wrapper

@bread
@lettuce
@tomatoes
@meat
def sandwich():
    pass

sandwich()