# Using a while loop to print even numbers less than 100
num = 0

while num < 100:
    if num % 2 == 0:
        print(num)
    num += 1

# Using a for loop to print even numbers less than 100
for num in range(0, 100, 2):
    print(num)