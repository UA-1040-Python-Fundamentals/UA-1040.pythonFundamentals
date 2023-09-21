# append method
strings = ['1', '2', '3', '4', '5', '7']
int_numbers = []

for i in range(len(strings)):
    int_numbers.append(int(strings[i]))
print(int_numbers)

# map method
strings = ['1', '2', '3', '4', '5', '7']
int_numbers = list(map(int, strings))
print(int_numbers)