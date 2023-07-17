a = input("Введіть значення для a: ")
b = input("Введіть значення для b: ")

list_operand = ["+", "-", "*", "/", "**", "//", "%"]

for i in list_operand:
    r = a + i + b
    result = eval(r)
    print(f"{a} {i} {b} = {result}")
