# # list
#
# l = list()
# print(type(l), l)
# l = list("test")
# print(type(l), l)
# # l = list(12) #error
# l = []
# print(type(l), l)
# l = [1, 2, 3, "test", 2.5, "p"]
# print(type(l), l)
# print(l[0])
# print(l[-1])
# # print(l[-8]) #error
# for i in l:
#     print(type(i), i)
# print(l[3])
# print(l[3][2])
# l.append(l)
# print(l[-1])
# print(l[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][0])
# print(l[1:3])
# print(l[1:6:2])
# print(l + [9, 8, 7])
# l[0] = 999
# print(l)
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)
# print(l1 is l2)
# l = [method for method in dir(list) if not method.startswith("_")]
# print(l)
# print([method for method in dir(list) if not method.startswith("_")])
# l = []
# for method in dir(list):
#     if not method.startswith("_"):
#         l.append(method)
# print(l)
# print(dir())
# print(dir(list))

# l = []
# l.append(1)
# l.append("test")
# print(id(l))
# l.append((1, 2, 3))
# print(l)
# print(id(l))
# l = l + [1]
# print(id(l))
# l = l + ["test"]
# print(id(l))
# l = l + [(1, 2, 3)]
#
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = []
# print(id(l), l)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9, l1, l2]
# print(l1)
# print(l2)
# print(l3)
# l1.clear()
# l2 = []
# print(l1)
# print(l2)
# print(l3)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9, l1, l2]
# t = l3.copy()
# # t = l3[:]
# print(id(l3), l3)
# print(id(t), t)
# l3[0] = 999
# t[0] = 777
# l3[3][0]="test"
# t[4][0]="foo"
# print(id(l3), l3)
# print(id(t), t)
# print(l1)
# print(l2)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9, l1, l2]
# l = [7, 8, 9, l1, l2]
# import copy
#
# t = copy.deepcopy(l3)
# # t = l3.copy()
# # t = l3[:]
# print(id(l3), l3)
# print(id(t), t)
# l3[0] = 999
# t[0] = 777
# l3[3][0] = "test"
# t[4][0] = "foo"
# print(id(l3), l3)
# print(id(t), t)
# print(l1)
# print(l2)
# # from lessons.lesson05.lesson05 import l as llll
# l.append(9)
# l.append([4, 5, 6])
#
# print(l)
# # print(llll)
# print(l.count(2))
# print(l.count(9))
# print(l.count([4, 5, 6]))
# print(len(l))
# print(l.__len__())

# l = []
# l.append("trest")
# l.append((1, 2, 3, 4))
# l.extend("trest")
# l.extend((1, 2, 3, 4))
# l.extend([1, 2, [1, 2, 3]])
# print(l)
#
# # print(l.index("t"))
# # print(l.index([1, 2, 3]))
# # print(l.index(1))
# # print(l.index(1,8))
# # print(l.index(1,8, 10))
# l.insert(99, 5)
# l.insert(-99, 5)
# l.insert(1, 5)
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(2))
# print(l)
# print(l.remove(1))
# print(l)
# l = [1,2,3,[1,2], 1, {1,2,3}]
# print(l)
# for i in l:
#     if type(i) in [list, set]:
#         while True:
#             try:
#                 i.remove(1)
#             except:
#                 break
#     else:
#         try:
#             l.remove(1)
#         except:
#             pass
# print(l)
# l.reverse()
#
# print(l)
# l = [1,2,43,3,2,4,5,43,3]
# l.sort()
# print(l)
# l = [1,2,43,3,2,4,5,43,3]
# ll = list(reversed(l))
# print(ll)
# ll = sorted(l)
# print(ll)
# print(l)
#
# ## tuple
#
# t = tuple()
# print(type(t), t)
# t = tuple("test")
# print(type(t), t)
# t = ()
# print(type(t), t)
#
# t = (1, 2, 3, 4)
# print(type(t), t)
# # t = (1) #int
# t = (1,)
# print(type(t), t)
# t = (1, 2, 9, 3, 4, 6, [11, 55])
# print(t[1])
# # t[1] = 33 #error
# t[-1][0] = 33
# print(t)
# print([method for method in dir(tuple) if not method.startswith("_")])
# print(sorted(t[:-1]))

# ## set
#
# s = set()
# print(type(s), s)
# s = set("vsdjbdjshkbdfjsvkdbvsfvhsbl")
# print(type(s), s)
# # s = {}
# # print(type(s), s)
# s = {1, 2, 3, 43, 2, 1, 2, 3, 4, 3, 2, "bghsdbj", "bghsdbj", "bghsdbj" }
# print(type(s), s)
#
# print([method for method in dir(set) if not method.startswith("_")])
# s.add(77)
# print(type(s), s)
# print(s.pop())
# s.update([1,2,3])
# print(s)

# dict

d = dict()
print(type(d), d)
d = dict([("key1", "value1"), ("key2", 2), (3, 33)])
print(type(d), d)
d = {}
print(type(d), d)
d = {
    "key1": "value1",
    "key2": 2,
    9: 33
}
print(type(d), d)
d[9] = 555
d["key2"] = 5555
d["key22"] = 5555
print(type(d), d)
# print(d["key223"])#error

print([method for method in dir(dict) if not method.startswith("_")])
print(d.fromkeys([1,2,3], 55))
print(d)
# print(d.get("key223"))
# print(d.get("key223", 99))
# print(d.get("key22"))
# print(d.get("key22", 99))
# print(d.items())
# for key in d:
#     print(key, d[key])
# a, b = 1,2
# for key, value in d.items():
#     print(key, value)
print(d.keys())
print(d.values())
v = d.pop("key22")
print(v, d)
print(d.popitem())
print(d)
d.setdefault("tet")
d["tat"] = None
print(d)
d.update({'key1': 'value1', 'key2': 5555, 9: 555, 'key22': 5555})
print(d)
