list_1 = [1, 2, 3, 4, 5]
print(list_1)
list_2 = list(map(float, list_1))
print(list_2)

# ----------------------------------------------------------------------------
list_2 = list()

for i in list_1:
    list_2.append(float(i))

print(list_2)
