even = []
odd = []
not_in_range = []

for num in range(1, 11):
    if num % 2 == 0:
        even.append(num)
    if num % 3 == 0 and num % 2 != 0:
        odd.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_in_range.append(num)

print("Even numbers divisible by 2:", even)
print("Odd numbers divisible by 3:", odd)
print("Numbers not divisible by 2 and 3:", not_in_range)