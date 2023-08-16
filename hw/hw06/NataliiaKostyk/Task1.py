even_div_2 = [n for n in range(1, 11) if n % 2 == 0]
odd_div_3 = [n for n in range(1, 11) if n % 2 == 1 and n % 3 == 0]
not_div_23 = [n for n in range(1, 11) if n % 2 >= 1 and n % 3 >= 1]

print(even_div_2)
print(odd_div_3)
print(not_div_23)
