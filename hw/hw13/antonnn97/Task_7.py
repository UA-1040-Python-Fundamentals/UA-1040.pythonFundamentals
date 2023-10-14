def lettuce_decorator(sandwich_func):
    def wrapper():
        print("<\ ^^^^^^^ />")
        sandwich_func()
        print("<\ ______ />")
    return wrapper

def tomato_decorator(sandwich_func):
    def wrapper():
        print("# tomato #")
        sandwich_func()
    return wrapper

def meat_decorator(sandwich_func):
    def wrapper():
        print("- meat -")
        sandwich_func()
    return wrapper

def salad_decorator(sandwich_func):
    def wrapper():
        print("~ salad ~")
        sandwich_func()
    return wrapper

# Base sandwich function
def base_sandwich():
    pass

# Build the sandwich
@lettuce_decorator
@tomato_decorator
@meat_decorator
@salad_decorator
def make_sandwich():
    base_sandwich()

# Create the sandwich
make_sandwich()