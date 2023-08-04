number_list = list(map(int, str(input())))
print(f'''
product of numbers - {number_list[0] * number_list[1] * number_list[2] * number_list[3]}
return - {number_list[::-1]}
''')

number_list.sort()
print('sort -', number_list)
