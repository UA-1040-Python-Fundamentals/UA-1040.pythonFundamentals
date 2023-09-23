'''Task1. Create a list that contains elements of integer type, then
use the loop to change the type of these elements to a floating
type.
(Hint: use the built-in float () function).'''

# Create a list with integer elements
integer_list = [1, 2, 3, 4, 5]

# Use a loop to convert the elements to floating-point numbers
float_list = []
for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print("Original list:", integer_list)
print("List with float elements:", float_list)