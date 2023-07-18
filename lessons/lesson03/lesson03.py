# a = "test"
# print(type(a), a)
# a = 13
# print(type(a), a)
# a = [1,2,3]
# print(type(a), a)
#
# i = 15
# print(id(i), i)
# i += 1
# print(id(i), i)
# l = []
# print(id(l), l)
# l.append(35)
# l.append(15)
# l.append(25)
# print(id(l), l)
# l.sort()
# print(id(l), l)

# for i in range(500):
#     print(id(i), i)
#     i = i + 1
#     i = i - 1
#     print(id(i), i)
# a = 15
# b = 15
# print(a is b)
# l1 = [1]
# l2 = [1]
# print(l1 is l2)
# print(id(l1) == id(l2))
# print(l1 == l2)
# a = int("1555")
# b = int("1555")
# print(a is b)
#
# for i in range(500):
#     s = str(i)
#     i1 = int(s)
#     i2 = int(s)
#     if i1 is i2:
#         print(i)
# s = "test1" \
#      "test2" \
#      "test3"
# print(s)
# s = ("test1"
#      "test2"
#      "test3")
# print(s)
# s = ["test1"
#      "test2"
#      "test3"]
# print(s)
# s = {"test1"
#      "test2"
#      "test3"}
# print(s)
# a=1;b=1;c=1
# a, b, c = 1, 2, 3
# a = b = c = 12
#
# a = []
# a.append(15)
# a.append(25)
# b = 13
# c = a[:]
#
#
#
# a = 0o07
# print(a)
# a = 0x09AF
# print(a)
# for i in range(33):
#     print(f"{bin(i)[2:].zfill(6)}\t{i}\t{oct(i)[2:].zfill(2)}\t{hex(i)[2:].zfill(2)}")

# f = 1.5
# print(f, type(f))
# f = .5
# print(f, type(f))
# f = 1.
# print(f, type(f))
# f = 15e1
# print(f)
# f = 15e-3
# print(f)

# print((-1)**0.5)

# a = 1
# b = True
# print(a is b)
# print(a == b)
#
# print(a+b)
# print(b+a)
#
# print(None is None)
# a = None

# l = [1, "test", 2.45, (1,2), {1, 2, 3, 1}]
# print(l)
# l[2] = 99.99
# print(l)
# print(l[1])
#
# l = (1, "test", 2.45, (1,2), [1, 2, 3, 1])
# print(l)
# # l[2] = 99.99#error
# # l[4] = {1, 2, 3, 1}#error
# l[4].append(4)
# print(l)
# a = l[4]
# a.append(5)
# print(l)
# d = {"key1": "value", "test":None}
# s="jhvdshjvdsjhbghdsfbvghdsbghjdsbgvkfdbd"
# print(set(s))
#
# for e in set(s):
#     print(e, s.count(e))

# d = {
#     (1, 2): 1,
#     "test": 2,
#     15: 25
# }
# print(d)
# print(d[15])
# print(d["test"])
# print(d[(1,2)])
# s="jhvdshjvdsjhbghdsfbvghdsbghjdsbgvkfdbd"
# d = {}
# for symbol in s:
#     if symbol in d:
#         d[symbol] += 1
#     else:
#         d[symbol] = 1
# print(d)
# print(s[2])
# print(s[2:5])
# print(s[2:15:2])
#
#
# s = list(range(20))
# print(s[2])
# print(s[2:5])
# print(s[2:15:2])
# d2 = {1:4}

# a = 9**4299
# print(a)

# a = int("15")
# print(a)
# a = int("101", 2)
# print(a)
# a = int("09az", 36)
# print(a)
# a = float("15")
# print(a)

#
# for i in range(256):
#     print(i, chr(i))
#
# s = "jhcvsdkh"
# for i in s:
#     print(i, ord(i))
#
# s = 'fasf\nasf\n\ng\nasgs\nafga'
# print(s)
# s = '''
# fasf
# asf
# g
# asgs
# afga
# '''
# print(s)
# s = """asdf
# sad
# asf
# asf
# """
# s = "bsdfjvhsd\"sdhbvjhdsb "
# print(s)

# s = "my name is %s, age %d"
# print(s % ("Liubomyr", 37))
# print(s % ("Andry", 25))
# print("%.2f" % 12.123456)
# print("%.3f" % 12.123456)
# print("%.10f" % 12.123456)
# s = "my name is {}, age {}"
# print(s.format("Liubomyr", 37))
# s = "my name is {name}, age {age} {name}"
# print(s.format(age= 37, name="Liubomyr"))
# name = "Liubomyr"
# print(f"my name is {name}, age {name}")
#
# s = "my NAMe is %s, age %d"
# print(s[len(s)-1])
# print(s[-1])
# print(s.lower())
# print(s.upper())
# print("=>".join(["my", "name", "is", "Liubomyr. age"]))
# print("my name is Liubomyr, age Liubomyr".split())
# print("my name is Liubomyr, age Liubomyr".split("a"))
# print("my name is Liubomyr, age Liubomyr".find("a"))
# print("my name is Liubomyr, age Liubomyr".find("a", 5))
# print("my name is Liubomyr, age Liubomyr".find("a", 5, 20))
# print("my name is Liubomyr, age Liubomyr".replace("a", "AAA"))
print(dir([]))
print(dir(""))
print(dir(tuple()))