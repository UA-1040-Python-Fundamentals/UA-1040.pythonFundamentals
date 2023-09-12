# Find the largest item in the list using the reduce function
from functools import reduce


numbers = [3, 9, 1, 7, 5,45, 100, 11, 8, 21, 9, 0, 4, -100]

def my_largest(x, y):
    return x if x > y else y

largest_item = reduce(my_largest, numbers)

print(largest_item)