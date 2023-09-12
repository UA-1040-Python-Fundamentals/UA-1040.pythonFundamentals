# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data.

class WeekError(Exception):
    pass

def week(number):
    week_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    print(f"You input number {number} it is {week_dict.get(number)}")

try:
    user_input = input("Enter day of the week: ")
    number = int(user_input)
    if number < 1 or number > 7:
        raise WeekError("Enter number from 1 to 7")
    week(number)
except ValueError:
    print("Error: Please enter a valid integer.")
except WeekError as e:
    print(f"Error: {e}")