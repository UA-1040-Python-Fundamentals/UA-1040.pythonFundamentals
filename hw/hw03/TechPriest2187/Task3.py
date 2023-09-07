#1
str = input()
#"better""never""is"
print(str.count('never')+str.count('better')+str.count('is'))
#uppercase
print(str.upper())
#replace()
print(str.replace('i','&'))

#2
num = input()
#digit_product
print(int(num[0])*int(num[1])*int(num[2])*int(num[3]))
#reverse_order
print(num[::-1])
#order
#??????

#3 - interchanging
a,b = 1,2
print(a,b)
a,b = b,a
print(a,b)