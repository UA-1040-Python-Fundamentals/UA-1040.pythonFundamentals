# Create a list of integers
integer_list = [1, 2, 3, 4, 5]

# Use a loop to change the type of each element to float
float_list = []
for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

# Print the original and the new float list
print("Original integer list:", integer_list)
print("List with float elements:", float_list)