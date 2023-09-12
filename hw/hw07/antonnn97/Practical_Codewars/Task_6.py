def reverse_list(l):
    'return a list with the reverse order of l'
    reversed_list = l[::-1]
    return reversed_list

input_list = [1, 2, 3, 4]
reversed_result = reverse_list(input_list)
print(reversed_result)