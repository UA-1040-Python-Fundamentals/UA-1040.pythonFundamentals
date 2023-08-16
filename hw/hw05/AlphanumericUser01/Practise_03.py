# Check if the list contains odd numbers.
# (Hint: use the break statement)

x = [0, 0, 6, 0, 1]
i = 0
flag = True
while i < len(x):
    flag = x[i] % 2 != 0
    if flag:
        break
    i += 1
if flag == True:
    print("The list contain odd number")
else:
    print("The list doesn't contain odd number")