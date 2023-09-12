def count_sheeps(array_of_sheep):
    return array_of_sheep.count(True)


sheep_list = [True, True, True, False, True, True, True, True,
              True, False, True, False, True, False, False, True,
              True, True, True, True, False, False, True, True]

sheep_count = count_sheeps(sheep_list)
print("Number of sheep present:", sheep_count)