# append method
str_numbers = ['1', '2', '3', '4', '5', '7']
int_numbers = []

for str_num in str_numbers:
    int_num = int(str_num)
    int_numbers.append(int_num)

print(int_numbers)

# map method
str_numbers = ['1', '2', '3', '4', '5', '7']

def str_to_int(str_num):
    return int(str_num)

int_numbers = list(map(str_to_int, str_numbers))

print(int_numbers)