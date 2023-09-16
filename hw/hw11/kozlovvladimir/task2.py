def calculate_the_divide_of_two_numbers(a, b):
    return a / b


try:
    a, b = map(int, input("Please enter number A and B: ").split(","))
    result = calculate_the_divide_of_two_numbers(a, b)
    print(f"{result}")
except ZeroDivisionError as error:
    print(f"Error: {error}")