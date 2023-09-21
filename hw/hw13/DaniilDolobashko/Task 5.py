from functools import reduce

colors = ["red", "gray", "yellow", "black", "blue"]

def get_largest(this_color, next_color):
    if len(this_color) > len(next_color):
        return this_color
    else:
        return next_color

largest = reduce(get_largest, colors)

print(largest)