# list()
#
# a = [1,2,3]

names = ["name1", "name2", "name3", ]
ages = [15, 96, 37]
sex = ["m", "m", "w"]

p = [{"name": "name1", "age": 15, "sex": "m"},
     {"name": "name2", "age": 96, "sex": "m"},
     {"name": "name3", "age": 37, "sex": "w"}]


# class M1:
#      def foo(self):
#           print("foo")
#
#
# class Human(M1):
#      pass
# h= Human()
# h.foo()

# class Human:
#      a= 1
#      """
#      this class impl human
#      """
#
# print(Human.__doc__)
# help(Human)
# print(Human.a)
# # print(a)#error


# class MyClass:
#      cm = []
#      ci = "Human"
#      def __init__(self):
#           self.im = []
#           self.ii = 15

# a1 = MyClass()
# a2 = MyClass()
# print(id(a1))
# print(id(a2))
# print(a1.cm, a1.ci, a1.im, a1.ii)
# print(a2.cm, a2.ci, a2.im, a2.ii)
# a1.cm.append("99")
# a1.im.append("66")
# a2.im.append("text")
# MyClass.ci = 88
# a2.ii = 33
# print(a1.cm, a1.ci, a1.im, a1.ii)
# print(a2.cm, a2.ci, a2.im, a2.ii)
#
# print(dir(MyClass))
# print(MyClass.__dict__)
# print(dir(a1))
# print(a1.__dict__)
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return f"name:{self.name} age:{self.age} sex:{self.sex}"
#
#     def __repr__(self):
#         return f"<{self.name}>"
#
#     def my_print(self):
#         print(self.name, self.age, self.sex )
#     def __del__(self):
#         print(f"del :{self}")
#
#
#
# h1 = Human("name1", 15, "m")
# h2 = Human("name2", 96, "m")
# h3 = Human("name3", 37, "w")
# print(h1)
# print(h2)
# print(h3)
# s1 = str(h1)
# print(s1)
# print([h1, h2, h3, 25])
# h1.my_print()
# h2.my_print()
# h3.my_print()
# print(Human.__dict__)
# print(h1.__dict__)
# print(h2.__dict__)
# print(h3.__dict__)
#
# Human.my_print(h1)
#
# p = Human.my_print
# p(h3)
#
# def my_f(obj, text=None):
#     print("my_f:", obj, text)
#
# my_f(h3)
# Human.foo = my_f
#
# h3.foo("text")

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f"({self.x}, {self.y})"
#
#     def print(self):
#         print(self, type(self))
#
#
#     def __add__(self, other):
#         p = Point()
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         return p
#
#     def add(self, other):
#         p = Point()
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         return p
#     def __lt__(self, other):
#         return self.x+self.y < other.x+other.y
#
# p1 = Point(3,78)
# p2 = Point(5,-5)
# p3 = p1 + p2
# print(p3)
# p4 = p3.add(p2)
# print(p4)
# # from pprint import pprint
# # pprint(Point.__dict__)
#
# p = [p1,p2,p3,p4]
# print(p)
# p.sort()
# print(p)
#
# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         self.z = z
#
#     def __repr__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#     def __add__(self, other):
#         p = Point3D()
#
#         p.x = self.x + other.x
#         p.y = self.y + other.y
#         p.z = self.z + other.z if type(other) is Point3D else 0
#         return p
#
#
# p3d = Point3D(10,20,30)
# print(p3d)
# p_z = p2 + p3d
# p2.print()
# p3d.print()
# p_z.print()
# p_z = p3d+p2
# p_z.print()
# p_z = p3d+p_z
# p_z.print()

# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(B, C): pass
# class F(D, E): pass
#
# print(F.__mro__)
#
# class MyClass:
#
#     def print(self):
#         print(f"inst: {self}  {type(self)}")
#
#     @classmethod
#     def print_class(cls):
#         print(f"inst: {cls}  {type(cls)}")
#
#     @staticmethod
#     def print_static():
#         print(f"inst: {}  {type(1)}")
#
#
# # MyClass.print()
# m = MyClass()
# m.print()
# m.print_class()
# MyClass.print_class()
# m.print_static()

# class MyClass:
#     # pass
#     def __init__(self,a,b,c):
#         self.x = a
#         self._x = b
#         self.__x = c
#     def __str__(self):
#         return f"{self.x=} {self._x=} {self.__x=}"
# y = MyClass(1,2,3)
# y = MyClass(1,2,3)
# y = MyClass(1,2,3)
# y = MyClass(1,2,3)
#
#
# print(y, y.__dict__)
# # print(y)
# # print(y.x)
# # print(y._x)
# # # print(y.__x)
# # print(y._MyClass__x)
class PointError(Exception):
    pass
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"({self.__x}, {self.__y})"

    def print(self):
        print(self, type(self))

    def __add__(self, other):
        p = Point()
        p.x = self.__x + other.__x
        p.y = self.__y + other.__y
        return p

    def add(self, other):
        p = Point()
        p.__x = self.__x + other.__x
        p.__y = self.__y + other.__y
        return p

    def __lt__(self, other):
        return self.__x + self.__y < other.__x + other.__y

    # def __get_x(self):
    #     print("get_x")
    #     return self.__x
    #
    # def __set_x(self, x):
    #     print("set_x", x)
    #     self.__x = x
    #
    # x = property(__get_x, __set_x)
    @property
    def x(self):
        print("get_x")
        return self.__x

    @x.setter
    def x(self, x):
        print("set_x", x)
        if type(x) is int:
            self.__x = x
        else:
            raise PointError()
    @property
    def y(self):
        print("get_y")
        return self.__y

    @y.setter
    def y(self, y):

        print("set_y", y)
        if type(y) is int:
            self.__y = y
        else:
            raise ZeroDivisionError("aaa")
    def get_info(self):
        pass

    getinfo = property(get_info)


p = Point(15, 22)
# print(p)
# print(p.get_x())
# p.set_x(99)
# print(p)
# print(p.x)
# p.x = 888
print(p)
p.y = "aa"
p.x = "aa"
print(p.y)
print(Point.getinfo)
print(Point.x)


