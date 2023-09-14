import math
def rectangle(a,b):
    return a*b
def triangle(a,h):
    return (1/2*a*h)
def circle(r):
    return round(math.pi*r**2,2)
print("Rectangle - 1\n"
      "Triangle - 2\n"
      "Circle - 3")
choice = int(input("Select a shape:"))
if choice == 1:
    print("Еhe area of the rectangle is", rectangle(a = int(input("Enter lenght: ")), b = int(input("Enter width: "))))
elif choice == 2:
    print("Еhe area of the triangle is",
    triangle(a = int(input("Enter the length of the side: ")),h= int(input("Enter height of the rectangle: "))))
elif choice == 3:
    print("Еhe area of the circle is", circle(r = int(input("Enter the radius of the circle: "))))
else:
    print("Wrong shape selected")