from functools import reduce

numbers = [3, 7, 1, 8, 10, 4, 6]

def find_max(x, y):
    return x if x > y else y

largest = reduce(find_max, numbers)

print("The largest item in the list is:", largest)
