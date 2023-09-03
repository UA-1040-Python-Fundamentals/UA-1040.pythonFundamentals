# print(a))
# print(0/0)
# print("test")
read = True
while read:
    a = input("a:")
    b = input("b:")
    read = False
    try:
        a = int(a)
        b = int(b)
        d = a / b
    except ZeroDivisionError as error:
        print()
        print("except", error.__class__.__mro__)
    except ArithmeticError as error:
        print("ArithmeticError => ", error)
    except ValueError as error:
        print("ValueError", error)
        read = True
    else:
        print(f"{d=}")
    finally:
        print("finally")
print("end")

def my_div(a, b):
    try:
        return a / b
    except:
        print("Error")
    finally:
        print("f")
        return 0
print(my_div(1, 2))