a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))

print(f'\n\rFirst number: {a}, Second number: {b}\n\r')

a,b = b,a

print(f'Numbers after interchange\n\rFirst number: {a}, Second number: {b}')