def divide_numbers():
    try:
        input_str = input("Enter two numbers separated by a comma: ")
        num1, num2 = map(float, input_str.split(','))

        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter two valid numbers separated by a comma.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result of {num1} / {num2} is: {result:.2f}")
    finally:
        print("Program execution completed.")

if __name__ == "__main__":
    divide_numbers()
