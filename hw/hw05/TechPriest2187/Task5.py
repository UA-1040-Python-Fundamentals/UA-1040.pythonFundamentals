# 1
list1 = list(range(10))
for i in range(len(list1)):
    float(list1[i])
print(list1)
# 2
n = int(input())
fibonacci = list(range(n))
for i in range(1, n):
    fibonacci[i + 1] = fibonacci[i] + fibonacci[i - 1]
    if fibonacci[i + 1] >= n:
        break
print(fibonacci[0:fibonacci.index(n) + 1])
# 3
num = int(input())
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)
