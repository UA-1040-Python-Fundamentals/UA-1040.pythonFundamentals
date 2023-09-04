import random

l_even = []
l_odd_3 = []
l_2_3 = []
for i in range(1, 10+1):
    if i % 2 == 0:
        l_even.append(i)
    elif i % 2 != 0 and i % 3 == 0:
        l_odd_3.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        l_2_3.append(i)
print(f"Even numbers that are divisible by 2: {l_even}")
print(f"Odd numbers, which are divisible by 3: {l_odd_3}")
print(f"Numbers that are not divisible by 2 and 3: {l_2_3}")

# for i in range(10):
#     if i % 2 == 0:
#         l_even.append(random.randint(-100, 100))
#     elif i % 2 != 0 and i % 3 == 0:
#         l_odd_3.append(random.randint(-100, 100))
#     elif i % 2 != 0 and i % 3 != 0:
#         l_2_3.append(random.randint(-100, 100))
# print(f"Even numbers that are divisible by 2: {l_even}")
# print(f"Odd numbers, which are divisible by 3: {l_odd_3}")
# print(f"Numbers that are not divisible by 2 and 3: {l_2_3}")



