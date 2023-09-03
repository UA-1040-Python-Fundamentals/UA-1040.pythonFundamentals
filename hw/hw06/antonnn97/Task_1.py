max_num = 10

print("Even numbers divisible by 2:")
for n in range(2, max_num + 1, 2):
    print(n)

print("Odd numbers divisible by 3:")
for n in range(3, max_num + 1, 3):
    print(n)

print("Numbers not divisible by 2 and 3:")
for n in range(2, max_num + 1):
    if n % 2 != 0 and n % 3 != 0:
        print(n)