#5.1
list = [1,2,3,5,6,7,8,9]
float_list = []
for i in list:
    i = float(i)
    float_list.append(i)
print(float_list)
#5.2
r1 = 0
r2 = 1
for i in range(10):
    print(r1,end = " ")
    r1, r2 = r2, r1 + r2

#5.3
print('\n')
f = 1
number = int(input("Input number: "))
for i in range(1,number):
    f = f*i
    print(f, end = ' ')
