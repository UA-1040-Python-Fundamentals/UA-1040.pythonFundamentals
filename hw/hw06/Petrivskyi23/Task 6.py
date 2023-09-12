# Task 6.1
even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0 and num % 3 != 0:
        even_divisible_by_2.append(num)
    elif num % 2 != 0 and num % 3 == 0:
        odd_divisible_by_3.append(num)
    elif num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)

print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 or 3:", not_divisible_by_2_or_3)


#Task 6.2
correct_login = "First"

user_login = input("Enter your login: ")

while user_login != correct_login:
    print("Error: Incorrect login. Please try again.")
    user_login = input("Enter your login: ")

print("Hello,", user_login + "! Welcome!")