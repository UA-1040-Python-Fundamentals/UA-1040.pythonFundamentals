#Task 5.1
integer_list = [1, 2, 3, 4, 5]

float_list = []
for num in integer_list:
    float_num = float(num)
    float_list.append(float_num)

print("Original integer list:", integer_list)
print("Converted float list:", float_list)


#Task 5.2
n = int(input("Enter a number n: "))

fibonacci_numbers = [0, 1]

while fibonacci_numbers[-1] + fibonacci_numbers[-2] <= n:
    next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_fibonacci)

print("Fibonacci numbers up to", n, ":", fibonacci_numbers)


#Task 5.3
number = int(input("please input number: "))
d = 1
factorial = 1
if number == 0:
    print(1)
else:
    for i in range(number):
        factorial = factorial * (d)
        d += 1
print(f'''Factorial of {number} is''',factorial)
