# DESCRIPTION:
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.

def on_board_computer() -> bool:
    """
    Asks for input of two values ​​and calculates whether there is enough fuel for the expected distance
    """

    user_distatnce = int(input("Enter you distance: "))
    user_fuel = int(input("Enter you rest_of_fuel: "))
    return True if user_fuel * 25 >= user_distatnce else False

print(on_board_computer())
