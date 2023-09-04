import numpy


data = input('Please enter number: ')

print(f'\n\rYour number is: {data}')
print('Product of the digits: ', numpy.prod(list(map(int, list(data)))))
print('Reverse order: ', data[::-1])

data = list(map(int, list(data)))
data.sort()
data = list(map(str, data))
print('Sorted digits: ', ''.join(data))
