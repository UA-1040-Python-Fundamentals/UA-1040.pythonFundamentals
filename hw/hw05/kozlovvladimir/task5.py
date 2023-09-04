# Task 5.1
ElementsOfIntegerType=list(range(6))
ElementsOfFloatingType = []
for iterating in ElementsOfIntegerType:
    iterating=float(iterating)
    ElementsOfFloatingType.append(iterating)
print(ElementsOfFloatingType)

# Task 5.2
n=int(input("Enter the number terms: "))
f=0
sum=1
if n<=0:
    print("The fibonacci series is: ",f)
else:
    print(f,sum,end=" ")
    for x in range(2,n):
        next=f+sum
        print(next,end=" ")
        f=sum
        sum=next

# Task 5.3
n = int(input("Enter the number:"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)