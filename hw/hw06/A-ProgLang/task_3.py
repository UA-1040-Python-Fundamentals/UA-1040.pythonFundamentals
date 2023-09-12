# Create a list of integers that are entered from the terminal and determine the maximum and minimum number among them.


# Initialize an empty list to store the entered integers
numbers = []

# Get input from the user until they enter an empty line
while True:
    try:
        user_input = input("Enter an integer (or press Enter to finish): ")

        # Check if the input is an empty line (user pressed Enter)
        if user_input == "":
            break

        # Convert the input to an integer and add it to the list
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Check if the list is not empty
if numbers:
    # Calculate the maximum and minimum numbers in the list
    max_num = max(numbers)
    min_num = min(numbers)

    # Print the results
    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")
else:
    print("No numbers were entered.")