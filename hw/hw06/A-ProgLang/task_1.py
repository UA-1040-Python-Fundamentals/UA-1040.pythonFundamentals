#Task1. In the range from 1 to 10 determine
#• even numbers that are divisible by 2,
#• odd numbers, which are divisible by 3,
#• numbers that are not divisible by 2 and 3.


# Initialize lists to store the results
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []

# Iterate through numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:  # Check if the number is even
        even_divisible_by_2.append(num)
    elif num % 3 == 0:  # Check if the number is odd and divisible by 3
        odd_divisible_by_3.append(num)
    else:
        not_divisible_by_2_or_3.append(num)

# Print the results
print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 or 3:", not_divisible_by_2_or_3)