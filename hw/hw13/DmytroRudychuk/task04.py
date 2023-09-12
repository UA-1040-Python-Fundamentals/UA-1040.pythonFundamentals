# Using several decorators, create a sandwich consisting of
# lettuce, tomatoes and meat.
# <\ ^^^^^^^ />
# # tomato #
# – meat–
# ~ salad ~
# <\ ______ />

def bread(func):
    def wrapper():
        print("<\ ^^^^^^^ />")
        func()
        print("<\ ______ />")
    return wrapper

def lettuce(func):
    def wrapper():
        print("~ salad ~")
        func()
    return wrapper

def tomato(func):
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
@tomato
@meat
@lettuce
def sandwich():
    pass

sandwich()

