def check_even_or_odd(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "even"
    else:
        return "odd"

try:
    age = int(input("Please enter your age: "))
    result = check_even_or_odd(age)
    print(f"Your age is {result}.")
except ValueError as error:
    print(f"Error: {error}")
