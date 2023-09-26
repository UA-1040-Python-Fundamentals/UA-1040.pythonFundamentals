def get_day_of_week(number):
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    if not isinstance(number, int):
        raise ValueError("Input must be a number.")

    if number < 1 or number > 7:
        raise ValueError("Input must be between 1 and 7.")

    return days_of_week[number - 1]


def main():
    try:
        number = int(input("Please enter a number (1-7): "))
        day = get_day_of_week(number)
        print(f"The day of the week is {day}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
