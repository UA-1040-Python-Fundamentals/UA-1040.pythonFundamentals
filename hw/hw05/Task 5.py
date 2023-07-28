# Task 5.1
print("Завдання 5.1")
list = [float(number) for number in range(15)]
print(list)

# Task 5.2
print("Завдання 5.2")
n = int(input("Введіть число до якого хочете порахувати число Фібоначі: "))

n1 = 0
n2 = 1

for i in range(n):
    if n == 0:
        print(n)
    else:
        print(n1)
        n1, n2 = n2, n1 + n2

# Task 5.3
print("Завдання 5.3")

while True:
    fact = 1
    n = int(input("Введіть число до якого хочете порахувати факторіал: "))
    try:
        for i in range(1, n+1):
            fact *= i
        print(f"Факторіал числа {n} = {fact}")
        break
    except ValueError:
        print("Значення перевищує довжину у 4300 символів")