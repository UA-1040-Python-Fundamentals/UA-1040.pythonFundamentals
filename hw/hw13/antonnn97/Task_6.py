def custom_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

for number in custom_range(1, 10, 2):
    print(number)