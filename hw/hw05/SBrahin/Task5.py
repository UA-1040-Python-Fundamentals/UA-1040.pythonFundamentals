# Завдання 1
myList = [1,4,5,7,8,9]
newList = [float(i) for i in myList]
print(newList)

# Завдання 2
s = int(input("Введіть до якого числа ви бажаєте отримати послідовність Фібоначі: "))
s = s - 1
firstNum = 0
secondNum = 1
for el in range(s):
    thirdNum = firstNum + secondNum
    firstNum,secondNum= secondNum,thirdNum
print(firstNum)

# Завдання 3
number = int(input("Введіть число для того щоб порахувати факторіал: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Факторіал числа {number} = {factorial}")

