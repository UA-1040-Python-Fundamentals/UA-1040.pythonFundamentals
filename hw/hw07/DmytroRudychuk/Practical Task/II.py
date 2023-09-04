# Program the function distance(p1, p2) which returns the distance between the points p1 and p2 in n-dimensional space. p1 and p2 will be given as arrays.

# Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of the same length or if both arrays are empty sets.

# If you don't know how to measure the distance between two points, go here: http://mathworld.wolfram.com/Distance.html

import math

def distance(p1, p2):
    """
    Calculates the distance between points p1 and p2 in n-dimensional space.
    Return: The distance between the points, or -1 if the arrays are not the same length or are empty.
    """

    # Check for the same length of arrays
    if len(p1) != len(p2):
        return -1
    
    # Check for empty arrays
    if len(p1) == 0:
        return -1
    
    
    # Calculation of the distance between points
    squared_distance = sum((x - y) ** 2 for x, y in zip(p1, p2))
    result = math.sqrt(squared_distance)
    
    return result