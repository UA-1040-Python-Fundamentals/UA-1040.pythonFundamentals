#Write a function that returns the arithmetic mean of any numbers of numbers

'''def arithmetic_mean (numbers):
    if not numbers:
        return None
    total = sum (numbers)
    mean = total/(len(numbers))
    return mean
numbers_list = [5,10,15,20,25]
average = arithmetic_mean(numbers_list)
print("The arithmetic mean is:", average)'''


def arithmetic_mean_manual_input():
    numbers = []

    while True:
        num_str = input("Enter a number (or 'done' to finish): ")
        if num_str.lower() == 'done':
            break
        try:
            num = float(num_str)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")

    if not numbers:
        return None

    total = sum(numbers)
    mean = total / len(numbers)
    return mean


average = arithmetic_mean_manual_input()
if average is None:
    print("No numbers entered.")
else:
    print("The arithmetic mean is:", average)