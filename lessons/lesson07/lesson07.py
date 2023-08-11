# def my_func(s):
#     a = s*5
#     print(a)
#     return a
# t = my_func("x")
# print(t)
# print(a)
#
# def my_f():
#     """
#     my func
#     :return: None
#     """
#     pass
# print(my_f)
# print(my_f())
# print(my_f.__doc__)
# print(my_f)
# # sum()
# help(my_f)

# s = 12
# r = s**s
# print(str(r)[:2])
# def f(s):
#     r = s ** s
#     return str(r)[:2]
#
#
# for i in range(10):
#     from random import randint
#     print(f(randint(1, 100)))

# def my_f():
#     return "test"
# print(my_f())
# print(my_f)
# f = my_f
# print(f())
# print(f)
# g = 1
# g()

# print(sum([1,2,3]))
# s = sum
# sum = 10
# print(sum)
# sum = s
# print(sum([1,2,3]))

# def my_f():
#     print(10)
#     return 25
#     print(30)
#
# print(my_f())
# def my_f():
#     for i in range(10):
#         print(i)
#         if i >3:
#             return 25
#     print(30)
#
# print("my_f=",my_f())
# def my_f():
#     for i in range(10):
#         print(i)
#     print(30)
# print("my_f=",my_f())
#
# def my_f():
#     for i in range(10):
#         print(i)
#         return None
#     print(30)
# print("my_f=",my_f())
# def my_f():
#     for i in range(10):
#         print(i)
#         return
#     print(30)
# print("my_f=",my_f())

# def my_f():
#     for i in range(10):
#         print(i)
#
# print("my_f=",my_f())
# def print_cv(name, age):
#     print(f"{name=} {age=}")
#
#
# # print_cv()#error
# # print_cv("Andry")#error
# # print_cv("Andry", 1, 99)  # error
# print_cv("Anrii", 19)
# print_cv( 19, "Anrii")


def print_cv(name, age, phone="+38"):
    print(f"{name=} {age=} phone=+{int(phone)}")


#
# # print_cv()#error
# # print_cv("Anrii")#error
# print_cv("Anrii", "19")
# print_cv("Anrii", 19, "0970")

# def print_cv(name, age, phone="+38"):
#     print(f"{name=} {age=} {phone=}")

# # print_cv()#error
# # print_cv("Anrii")#error
# print_cv("Anrii", "19")
# print_cv("Anrii", 19, "0970")
# # print_cv("Anrii", 19, "0970", "ss")#error


# def print_cv(name="Empty", age, phone="+38"): #error
#     print(f"{name=} {age=} {phone=}")


# def print_cv(name, age, phone="+38"):
#     print(f"{name=} {age=} {phone=}")
# # print_cv("Anrii", "19")
# # print_cv("Anrii", 19, "0970")
# # print_cv( 19, "0970", "Anrii")
# # print_cv( age=19, phone="0970", name="Anrii")
# # print_cv( age=19, phone="0970", "Anrii")
# print_cv( "Anrii", phone="0970", age=25)

# def print_cv(name, age, *phones):
#     print(f"{name=} {age=} {phones=}")
#
#
# print_cv("Anrii", 25, 1, 2, 3, 4, 5, 6)

# def print_cv(name, age, *phones, adress="Lviv"):
#     print(f"{name=} {age=} {phones=} {adress=}")
#
#
# print_cv("Anrii", (25,2,3,), 1, 2, 3, 4, 5, 6, adress="Busk")
# # print_cv("Anrii", 25, 1, 2, 3, 4, 5, 6, adress="Busk", tt="error")
#
# def print_cv(name, age, *phones, adress="Lviv", **kwargs):
#     print(f"{name=} {age=} {phones=} {adress=} {kwargs=}")
#
# print_cv("Anrii", 25, 1, 2, 3, 4, 5, 6, adress="Busk", tt="error", tt2="error2")
# def my_all(*args, **kwargs):

# def print_cv(name, age,  adress="Lviv", *phones, **kwargs):
#     print(f"{name=} {age=} {phones=} {adress=} {kwargs=}")
# # print_cv("Anrii", (25,2,3,), 1, 2, 3, 4, 5, 6, adress="Busk")
# print_cv("Anrii", (25,2,3,), 1, 2, 3, 4, 5, 6, )
#
# def print_cv(name, age, *phones, adress="Lviv", **kwargs):
#     print(f"{name=} {age=} {phones=} {adress=} {kwargs=}")
#
#
# print_cv("Anrii", (25, 2, 3,), 1, 2, 3, 4, 5, 6)
# l = ("Anrii", (25, 2, 3,), 1, 2, 3, 4, 5, 6)
# print_cv(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
# print_cv(*l)
# d = {
#     "age": 16,
#     "adress": "Ivo",
#     "name": "Vasa",
#     "test": "test"
# }
# print_cv(d["name"], d["age"], adress=d["adress"], test=d["test"])
# print_cv(*d)
# print_cv(name=d["name"], age=d["age"], adress=d["adress"], test=d["test"])
# print_cv(**d)
# def mein(*args):
#     return sum(args) / len(args)
#
#
# print(mein(1, 22, 55, 88, 6))
#
#
# def arif_mean(*args):
#     return sum(args) / len(args)
#
#
# print(arif_mean(1, 2, 3, 4, 6, 3))
# x = 20
# print(dir())
# def scope_func():
#     print(dir())
#     x = 10
#     print(dir())
#     print("Value inside function:", x)
#
#
#
# scope_func()
# print("Value outside function:", x)
#
# def f(x):
#     x = 99
#     print("Value inside function:", x)
# f(x)
# print("Value outside function:", x)
# x= [1]
# def f(x):
#     x = 10
#     print("Value inside function:", x)
# f(x)
# print("Value outside function:", x)

# y = 99
# x= [1]
# def f():
#     print("Value inside function:", y)
#     print("Value inside function:", x)
#     x = 10
#     print("Value inside function:", x)
# f()
# print("Value outside function:", x)
#
# y = 99
# x= [1]
# def f():
#     global x
#     print("Value inside function:", y)
#     print("Value inside function:", x)
#     x = 10
#     print("Value inside function:", x)
# f()
# print("Value outside function:", x)
#
# def f():
#     def ff():
#         def fff():
#             global x
#             print("Value inside function:", y)
#             print("Value inside function:", x)
#             x = 888
#             print("Value inside function:", x)
#         fff()
#     ff()
#
# f()
# print("Value outside function:", x)
#
# def f():
#     l = 10
#     def ff():
#         l = 20
#         def fff():
#             nonlocal l
#             l = 99
#             print(l)
#         fff()
#         print(l)
#     ff()
#     print(l)
#
# f()
def fun():
    count = 0

    def my_f(*args):
        nonlocal count
        count += 1
        print(f"function run: {count}")
        return sum(args)

    return my_f


f = fun()
print(id(f))
f2 = fun()
print(id(f2))
# print(f(1,2,34,54))
# print(f2(1,2,34,54, 55))
# print(f(1,2,34,54, 55))
# print(f(1,2,34,54, 55))
# print(f2(1,2,34,54, 55))
count = 0


def my_f(*args):
    global count
    count += 1
    print(f"function run: {count}")
    return sum(args)


def fun():
    return my_f


f = fun()
print(id(f))
f2 = fun()
print(id(f2))
print(f(1, 2, 34, 54))
print(f2(1, 2, 34, 54, 55))
print(f(1, 2, 34, 54, 55))
print(f(1, 2, 34, 54, 55))
print(f2(1, 2, 34, 54, 55))
