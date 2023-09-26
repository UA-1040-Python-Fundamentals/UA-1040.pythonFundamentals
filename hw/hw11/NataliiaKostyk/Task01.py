def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age % 2 == 0:
        return f"Your age is {age}, which is an even number."
    else:
        return f"Your age is {age}, which is an odd number."


age = int(input("Please enter your age: "))
print(age)
try:
    result = check_age(age)
    print(result)
except ValueError as e:
    print(e)
