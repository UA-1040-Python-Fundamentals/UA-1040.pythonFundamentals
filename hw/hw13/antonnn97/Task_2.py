colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

def is_red(item):
    return item == "red"

red_items = list(filter(is_red, colors))

print(red_items)