# All these numbers in the list have a string data type, for example
# ['1', '2', '3', '4', '5', '7'], convert this list to a list, all numbers of
# which have the data type integer :
# 1) using the append method
# 2) using the map method

string_list = ['1', '2', '3', '4', '5', '7']
int_list = []
list_comprehension = [int_list.append(int(x)) for x in string_list]

int_list_map = list(map(int, string_list))

print(int_list)
print(int_list_map)