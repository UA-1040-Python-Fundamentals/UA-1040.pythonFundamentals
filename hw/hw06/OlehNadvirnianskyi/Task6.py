#Task1
print("Even numbers that are divisible by 2:")
for x in range (1,11):
    li= []
    if x %2 ==0:
        li.append(x)
        print(li,end="")

print("\nOdd numbers, which are divisible by 3:")
for y in range (1,11):
    l=[]
    if y %3 ==0:
        l.append(y)
        print(l, end="")


print("\nNumbers that are not divisible by 2 and 3:")
for z in range (1,11):
    si = []
    if z % 3 == 1 and z % 2 == 1:
        si.append(z)
        print(si, end="")

#Task 2
mail= {"login":"First"}
while True:
    user_email = input("\n Enter your e-mail:")
    if user_email == mail["login"]:
        print("Hello!")
        break
    else:
        print("Invalid email! Try again.")
