def checking_number(number):
    if not number.isdigit():
        raise ValueError("You entered nonnumerical data.")
    if int(number) > 7 or int(number) < 1:
        raise ValueError("Number cannot be less than 1 or more than 7.")
    if int(number) == 1:
        return "Monday"
    elif int(number) == 2:
        return "Tuesday"
    elif int(number) == 3:
        return "Wednesday"
    elif int(number) == 4:
        return "Thursday"
    elif int(number) == 5:
        return "Friday"
    elif int(number) == 6:
        return "Saturday"
    elif int(number) == 7:
        return "Sunday"

try:
    number = input("Please enter number: ")
    result = checking_number(number)
    print(f"Today is {result}.")
except ValueError as error:
    print(f"Error: {error}")