# a = 1
# b = 2
# c = 3
#
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)

# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
#
#
# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

# is_false = [False, 0, None, [], {}, (), ""]
# # print(True and 5 and "test")
# # print(True and [] and "test")
# # print(True and [] and False and "test")
# # print(True and False and [] and "test")
# print(False or 0 or {})
# print(False or 1 or {})
# print(False or 22 or 1 or {})
# a = True and 5 and "test"
# print(a)

# print("15" is "15")
# print(True is 1)
# l1 = [1,2,3]
# l2 = [1,2,3]
# print(id(l1), id(l2))
# print(id(l1) == id(l2))
# print(l1 == l2)
# print(l1 is l2)
# print(l1 is not l2)
# s1 = "15"
# s2 = "15"
# s3 = "1"
# s4 = "5"
# s5 = s3+s4
# print(id(s1), id(s2))
# print(id(s5))

# print(5 in 15)#error
# print(5 in [1, 5, 3, 5])
# print([1, 2] in [1, 2, 5, 3, 5])
# print([1, 2] in [1, 2, 5, 3, 5, [1, 2]])
# a = 7
# print(a > 5 and a < 10)
# print(5 < a < 10)
# a, b, c, d = 1, 2, 3, 4
# print(a < b < c < d)

a = int(input("a:"))
# if 5 <= a < 10:
#     print("a is [5, 10)")
#     print("a is [5, 10)")
#     print("a is [5, 10)")
# print("end")

# if 5 <= a < 10:
#     print("\ta is [5, 10)")
# else:
#     print("\ta is not [5, 10)")
# print("end")
#
# if a < 0:
#     print("a is negative")
# else:
#     if a == 0:
#         print("a is zero")
#     else:
#         print("a is positive")

# if a < 0:
#     print("a is negative")
# elif a == 0:
#     print("a is zero")
# elif a == 12:
#     print("a is 12")
# else:
#     print("a is positive")


# if a < 0:
#     print("a is negative")
# elif a == 0:
#     print("a is zero")
# elif a == 12:
#     print("a is 12")
#  a>b ? True: False
# t = True if a>b else False
#
# if a>b:
#     t = True
# else:
#     t = False
#
# r = t = None
# label t1
# if a > 10:
#
#     if a > 10:
#
#         if a > 10:
#             go to t2
#             r = a ** 8
#
# print(t)
# print(r)
#ToDo
# label t2
if a < 0:
    print("a is negative")
elif a == 0:
    print("a is zero")
elif a == 12:
    print("a is 12")
else:
    print("a is positive")

match a:
    case [0, 15, "test", a,[1,2,3]]:
        print("a is zero")

    case 1 | 3:
        print("===")
    case 1:
        print("===")
    case 3:
        print("===")
    case _:
        pass
# def f1(a,b):
#     return a+b
# def f2(a,b):
#     return a*b
#
# d={"1": f1,
#    "2": f2}
# d["1"](15, 12)
