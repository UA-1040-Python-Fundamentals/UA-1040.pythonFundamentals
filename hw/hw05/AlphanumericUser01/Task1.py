# Task1. Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function)

x = list(map(int, input('please enter integer elements: ').split()))
print(x)
i = 0
while i < len(x):
    x[i] /= 1
    i += 1
print(x)
