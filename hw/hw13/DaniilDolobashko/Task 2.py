def check_red(color):
    if color == "red":
        return True
    return False

color_list = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]

reds = filter(check_red, color_list)

reds = list(reds)

print(reds)