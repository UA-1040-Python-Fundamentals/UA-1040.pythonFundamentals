#-------------------------------- Task 7.1 ---------------------------------------

def largest_long_numb(*numbers):
    """This function return the largest(longest) number of numbers"""
    numbers = []
    largest_num = 0
    len_list = [0]

    while True:
        number = input("Enter your numbers (or press Enter to finish): ")

        if number == "":
            break

        try:
            number1 = float(number)
            numbers.append(number1)
        except ValueError:
            print("Invalid input. Please enter a valid number")

    for i in numbers:
        len_num = len(str(i))
        if len_num > max(len_list):
            largest_num = i
        len_list.append(len_num)

    return (f"The largest(longest) numb is: {largest_num}")

print(largest_long_numb())

print("--"*10)
print("The next function")


def largest_big_numb(*numbers):
    """This function return the largest(biggest) number of numbers"""
    numbers = []
    while True:
        number = input("Enter your numbers (or press Enter to finish): ")

        if number == "":
            break

        try:
            number1 = float(number)
            numbers.append(number1)
        except ValueError:
            print("Invalid input. Please enter a valid number")
    
    return (f"The largest number is: {max(numbers)}")

print(largest_big_numb())

#-------------------------------- Task 7.2 ---------------------------------------



#-------------------------------- Task 7.3 ---------------------------------------