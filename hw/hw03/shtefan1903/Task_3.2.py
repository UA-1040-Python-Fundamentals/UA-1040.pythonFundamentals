number = input("Enter a four-digit natural number: ")
list1 = list(number)
product = int(list1[0]) * int(list1[1]) * int(list1[2]) * int(list1[3])
print(product)
print(list(reversed(list1)))
print(sorted(list1))

