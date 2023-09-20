def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        return "even"
    else:
        return "odd"


def main():
    try:
        age = int(input("Please enter your age: "))
        result = check_age(age)
        print(f"Your age is {result}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
