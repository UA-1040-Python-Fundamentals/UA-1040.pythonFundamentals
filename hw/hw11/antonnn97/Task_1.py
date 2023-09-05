def get_day_of_week(number):
    if not number.isdigit():
        return "Please enter a number."

    number = int(number)
    if number < 1 or number > 7:
        return "Invalid input. Enter a number between 1 and 7."

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[number - 1]

try:
    input_number = input("Enter a number (1-7) to get the day of the week: ")
    result = get_day_of_week(input_number)
    print(result)
except ValueError:
    print("Invalid input. Please enter a numerical value.")