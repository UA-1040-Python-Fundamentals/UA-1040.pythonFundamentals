#Task 6.1
lst1 = []
lst2 = []
lst3 = []
for i in range(1,10):
    if i % 2 == 0:
        lst1.append(i)
    elif i % 2!=0 and i % 3 == 0:
        lst2.append(i)
    else:
        lst3.append(i)
print(lst1,lst2,lst3,sep="\n")

#Task 6.2
login = input("Enter login: ")
while login != "First":
    print("Welcome!")
else:
    print('Incorrect login. Please try again.')