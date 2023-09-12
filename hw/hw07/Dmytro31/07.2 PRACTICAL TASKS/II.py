import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

# Example usage
x1 = 1
y1 = 2
x2 = 4
y2 = 6

distance = calculate_distance(x1, y1, x2, y2)
print("Distance:", distance)