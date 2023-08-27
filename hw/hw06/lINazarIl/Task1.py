even_numbers = [x for x in range(1, 11) if x % 2 == 0 ]
print('Even numbers: ',even_numbers)

odd_numbers = [x for x in range(1, 11) if x % 2 > 0 and x % 3 == 0]
print('Odd numbers divisible by 3: ', odd_numbers)

ndbtat_numbers = [x for x in range(1, 11) if x % 2 > 0 and x % 3 > 0]
print('Numbers that are not divisible by 2 and 3: ', ndbtat_numbers)