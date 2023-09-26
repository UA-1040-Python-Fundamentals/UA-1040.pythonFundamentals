days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}

number = (input("Please enter a number: "))

try:
    number = int(number)
    day = days[number]
    print(f"The day corresponding to {number} is {day}.")
except KeyError:
    print(f"There is no day corresponding to {number}. Please enter a number between 1 and 7.")
except ValueError:
    print(f"Invalid input. Please enter an integer.")
