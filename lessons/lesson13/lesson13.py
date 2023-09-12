# l = [i for i in range(5)]
# s = {i for i in range(5)}
# d = {i: i for i in range(5)}
# print(l, s, d)
# t = (i for i in range(5))
# print(t)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
#
# print(l.__sizeof__())
# print(t.__sizeof__())
# N = 1200
# t = (i for i in range(N))
# l = [i for i in range(N)]
# print(l.__sizeof__())
# print(t.__sizeof__())
#
# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# vec3 = [15, -20, 5, 1]
# print(list(zip(vec1, vec2)))
# print(list(zip(vec1, vec2, vec3)))
# dot_mul = [u * v for u, v in zip(vec1, vec2)]
# print(dot_mul)
#
# import random
#
# names = ['Sam', 'Don', 'Sid']
# code_names = ['Iron', 'Batman', 'Capitan']
# secret_names = map(lambda x: f"{random.choice(code_names)}_{x}", names)
#
#
# def my_f(obj):
#     pass
#
#
# # secret_names = map(my_f, names)
# # secret_names = map(random.choice(code_names), names)
# print(list(secret_names))
#
#
# def isPos(number):
#     return number > 0
#
#
# a = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
# print(list(filter(isPos, a)))
# print(list(filter(lambda x: x > 0, a)))
# from functools import reduce
#
#
# def con(first, second):
#     print(f"{first=} {second=}")
#     return f"{first}_{second}"
#
#
# print(reduce(con, ["test1", "test2", "test3", "test4"]))
# print(reduce(con, ["test1", "test2", "test3", "test4"], "FOO"))

# class MyNumbers:
#     def __init__(self, num):
#         self.num = num
#     def __iter__(self):
#         print("__iter__")
#         self.a = 0
#         return self
#     def __next__(self):
#         print("__next__")
#         x = self.a
#         self.a += 1
#         if self.a > self.num:
#             # return
#             raise StopIteration
#             # raise Exception
#         return x
#
# t = MyNumbers(10)
# print("_"*3)
# for i in t:
#     print(i)

# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'
# e = my_generator()
# print(e)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
#
# def my_generator(n):
#     print(f"run {n=}")
#     i = 0
#     print(f"init {i=}")
#     while True:
#         print(f"start iter")
#         if n<i:
#             return
#         print(f"yield {i=}")
#         yield i
#         print(f"new yield iter")
#         i += 1
#         print(f"end iter")
# g = my_generator(4)
# print(g)
# print("-"*10)
# print(next(g))
# print("-"*10)
# print(next(g))
# print("-"*10)
# print(next(g))
# print("-"*10)
# print(next(g))
# print("-"*10)
# print(next(g))
# print("-"*10)
# # print(next(g))
# for i in my_generator(4):
#     print(f"{i=}")
#
# def star(fun):
#     print("*" * 20)
#     # fun()
#     print(fun)
#     print("*" * 20)
#     return fun
#
#
# star(15)
#
#
# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(324, 65))


# @star
# def my_sum(a, b):
#     return a + b

# def my_sum(a, b):
#     return a + b
# my_sum = star(my_sum)
#
#
# my_sum(324, 65)

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#
#     return inner
#
#
# def percent(func):
#     print(f"func {id(func)}")
#     def inner(*args, **kwargs):
#         lo
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#
#     print(f"inner {id(inner)}")
#     return inner
#
#
#
# @percent
# def my_sum(a, b):
#     return a + b
# # my_sum = percent(my_sum)
# print(id(my_sum))


from my_log import my_log


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @my_log
    def print(self):
        print(self, type(self))

    @my_log
    def __add__(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p

    @my_log
    def add(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p

    @my_log
    def __lt__(self, other):
        return self.x + self.y < other.x + other.y


p1 = Point(3, 78)
p2 = Point(5, -5)
print(p2)
p3 = p1 + p2
print(p3)
p4 = p3.add(p2)
print(p4)
def dec(file_name, mode="a"):
    def wrapper(fun):
        def inner(*args, **kwargs):
            f = open(file_name, mode)
            f.writelines(f"{fun} {args} {kwargs}")
            f.close()
            return fun(*args, **kwargs)
        return inner
    return wrapper

@dec("my_file.txt")
@my_log
def add_points(*points):
    p = Point()
    for point in points:
        p += point
    return p

@dec("my_file2.txt")
def add_points2(*points):
    p = Point()
    for point in points:
        p += point
    return p


s = add_points(p1, p2, p3, p4)
s = add_points2(p1, p2, p3, p4)


