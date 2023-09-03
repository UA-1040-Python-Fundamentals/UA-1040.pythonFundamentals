even_divisible_by_2 = [a for a in range(1, 11) if a % 2 == 0]
odd_divisible_by_3 = [a for a in range(1, 11) if a % 2 == 1 and a % 3 == 0]
not_divisible_by_2_and_3 = [a for a in range(1, 11) if a % 2 != 0 and a % 3 != 0]

print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_and_3)
