def bread(func):
    def wrapper():
        print("<\\", "^" * 7, "/>")
        func()
        print("<\\", "_" * 7, "/>")
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

def salad(func):
    def wrapper():
        print("~ salad ~")
        func()
    return wrapper

@bread
@tomatoes
@meat
@salad
def sandwich():
    pass

sandwich()
