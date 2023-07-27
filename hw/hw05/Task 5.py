# Task 5.1
list = [float(number) for number in range(15)]
print(list)

# Task 5.2

n = int(input("Введіть число до якого хочете порахувати число Фібоначі: "))

n1 = 0
n2 = 1

for i in range(n):
    if n == 0:
        print(n)
    else:
        print(n1)
        n1, n2 = n2, n1 + n2