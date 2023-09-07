n = int(input('Please enter the number: '))

result = 1

for i in range(1, n+1):
    result *= i
    print(i, result)

print(f'Result: {result}')