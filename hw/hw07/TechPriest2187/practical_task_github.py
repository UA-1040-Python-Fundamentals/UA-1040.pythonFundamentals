#1
def max(a,b):
    lst = [a,b]
    c = max(a,b)
    return c

print(max(2,3))
#2
def Tri_area(a,c):
    return (a*c)/2

def Circ_area(r):
    return 3.14*r*r

def Rect_area(a,b):
    return a*b

print("type of area:")
type = input()
if type == "Tri":
    print(Tri_area(int(input()),int(input())))
elif type == "Rect":
    print(Rect_area(int(input()),int(input())))
elif type == "Circ":
    print(Circ_area(int(input())))
#3
def Nums(word):
    lets = set()
    for i in range(len(word)):
        lets.add(word[i])

    dict  = {}
    for i in range(len(lets)):
        dict[lets[i]] = word.count(lets[i])
    return dict


