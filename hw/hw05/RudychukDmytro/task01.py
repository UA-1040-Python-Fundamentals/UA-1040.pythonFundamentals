import random


int_list = [random.randint(-10, 10) for _ in range(5)]
float_list = []
for i in int_list:
    float_list.append(float(i))
print(float_list)
