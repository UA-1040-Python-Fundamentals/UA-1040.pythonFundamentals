integer_list = [5, 10, 15, 20, 25]

float_list = []
for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print("Original integer list:", integer_list)
print("Converted float list:", float_list)