def count_sheeps(sheep):
    count = 0

    for is_present in sheep:
        if is_present == True:
            count += 1

    return count


sheep_array = [True, True, True, False, True, True, True, True,
               True, False, True, False, True, False, False, True,
               True, True, True, True, False, False, True, True]

result = count_sheeps(sheep_array)
print("The number of present sheep is:", result)