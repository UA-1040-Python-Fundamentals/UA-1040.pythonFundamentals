def two_points(x1, x2, y1, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


print(two_points(1, 2, 1, 2))
