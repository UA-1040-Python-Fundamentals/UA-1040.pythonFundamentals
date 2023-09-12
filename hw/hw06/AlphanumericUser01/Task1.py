# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

even_nm = []
odd_nm = []
numbers = []
a = 0
for x in range (1, 10):
    if x % 2 == 0:
        even_nm.append(x)
    elif x % 3 == 0:
        odd_nm.append(x)
for a in range(1, 10):
    if a not in odd_nm and a not in even_nm:
        numbers.append(a)
print(even_nm)
print(odd_nm)
print(numbers)
