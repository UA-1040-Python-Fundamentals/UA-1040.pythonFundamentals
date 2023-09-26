def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        number = int(input("Please enter an integer: "))
        result = is_even_or_odd(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()