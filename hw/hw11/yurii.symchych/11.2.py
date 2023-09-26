try:
    input_str = input("Enter two numbers separated by a comma (e.g., 5, 2): ")
    num1_str, num2_str = input_str.split(',')
    num1 = float(num1_str.strip())
    num2 = float(num2_str.strip())

    result = num1 / num2

except ValueError as ve:
    print(f"ValueError: {ve}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An exception occurred: {e}")
else:
    print(f"The result of {num1} / {num2} is: {result}")
finally:
    print("Program execution completed.")
