def get_day_of_week(number):
    try:
        number = int(number)
        if 1 <= number <= 7:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return days[number - 1]
        elif number >= 8:
            return "Invalid day (out of range)"
        else:
            return "Invalid input (negative number)"
    except ValueError:
        return "Invalid input (not a number)"


def main():
    user_input = input("Enter a number (1-7) to get the day of the week: ")
    result = get_day_of_week(user_input)
    print(f"Day of the week: {result}")


if __name__ == "__main__":
    main()
