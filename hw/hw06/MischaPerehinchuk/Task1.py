
couples = []
odd = []
others = []

for num in range(1, 11):
    if num % 2 == 0:
        couples.append(num)
    elif num % 3 == 0:
        odd.append(num)
    else:
        others.append(num)

print("Парні числа, які діляться на 2:", couples)
print("Непарні числа, які діляться на 3:", odd)
print("Числа, які не діляться на 2 і 3:", others)
