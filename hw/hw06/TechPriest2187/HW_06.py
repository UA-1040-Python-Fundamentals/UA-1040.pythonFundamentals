lstDiv2 = list()
lstDiv3 = list()
lstNonDiv23 = list()
for i in range(10):
    if i % 2 == 0:
        lstDiv2.append(i)
    elif i % 3 == 0 and i % 2 != 0:
        lstDiv3.append(i)
    elif i %2 != 0 and i % 3 != 0:
        lstNonDiv23.append(i)

print(lstDiv2,lstDiv3,lstNonDiv23)