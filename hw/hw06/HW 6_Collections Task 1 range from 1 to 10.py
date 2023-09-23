'''Task1. In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.'''
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0:
        even_divisible_by_2.append(num)
    if num % 2 != 0 and num % 3 == 0:
        odd_divisible_by_3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)

# Create a dictionary to store the results using appropriate collections
results_dict = {
    'even_divisible_by_2': even_divisible_by_2,
    'odd_divisible_by_3': odd_divisible_by_3,
    'not_divisible_by_2_or_3': not_divisible_by_2_or_3
}

# Print the results using the dictionary
for category, numbers in results_dict.items():
    print(f"{category.replace('_', ' ').title()}: {numbers}")