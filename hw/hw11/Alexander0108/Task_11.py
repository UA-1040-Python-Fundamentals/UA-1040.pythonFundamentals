
#------------------------------------ Task 11.1 -----------------------------------------

def isodd(number=int):
    try:
        if number % 2 == 0:
            return f"{number} is odd"
        else:
            return f"{number} is even"
    except Exception as a:
        return f"Error: {a}"
    
print(isodd(24))
print(isodd("2321"))

#------------------------------------ Task 11.2 -----------------------------------------

while True:
    try:
        input_str = input("Enter two numbers separated by a comma (x,y): ")
        x, y = map(float, input_str.split(','))  # Split the input and convert to float
        result = x / y

    except ValueError:
        print("Error: Please enter valid numeric values separated by a comma.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print(f"The result of {x} / {y} is {result}")
        break  # Exit the loop if no exceptions are raised

    finally:
        print("Execution completed.")

#------------------------------------ Task 11.3 -----------------------------------------

def checkage(age):
    if age < 0:
        raise ValueError("Input must be a positive number")
    else:
        if age % 2 == 0:
            return f"Your age: {age} is odd"
        else:
            return f"Your age: {age} is even"

print(checkage(21))    
print(checkage(-15))

#------------------------------------ Task 11.4 -----------------------------------------

def get_day_of_week():
    try:
        num = int(input("Enter a number (1-7) to get the day of the week: "))
        
        if 1 <= num <= 7:
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            day = days_of_week[num - 1]
            print(f"The day corresponding to {num} is {day}.")
        else:
            print("Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

