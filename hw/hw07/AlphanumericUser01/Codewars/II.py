# DESCRIPTION:
# Given two ordered pairs calculate the distance between them.
# Round to two decimal places.
# This should be easy to do in 0(1) timing.

import math

def distance(x1, y1, x2, y2):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dis, 2)


a = distance(1, 2, 3, 4)
print(a)
