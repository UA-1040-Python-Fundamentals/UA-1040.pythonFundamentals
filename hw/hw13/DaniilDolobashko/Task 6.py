def my_range(start_number, finish_number, step = 1):
    current = start_number
    while current < finish_number if step > 0 else current > finish_number:
        yield current
        current += step

# Example usage:
for i in my_range(0, 15, 2):
    print(i)