for num in range(1, 11):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is even and divisible by 2 and 3")
    elif num % 2 == 0:
        print(f"{num} is even and divisible by 2")
    elif num % 3 == 0:
        print(f"{num} is odd and divisible by 3")
    else:
        print(f"{num} is neither divisible by 2 nor 3")