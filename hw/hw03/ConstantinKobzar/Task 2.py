def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def reverse_number(number):
    return int(str(number)[::-1])

def ascending_order_number(number):
    return int(''.join(sorted(str(number))))

def sort_digits_included(number):
    sorted_digits = sorted(str(number))
    return int(''.join(sorted_digits))

def main():
    try:
        # Taking input from the user
        num = int(input("Enter a four-digit natural number: "))

        # Check if the number is four digits
        if 1000 <= num <= 9999:
            # Calculate the product of digits
            product = product_of_digits(num)
            print("Product of digits:", product)

            # Reverse the number
            reversed_num = reverse_number(num)
            print("Reversed number:", reversed_num)

            # Number in ascending order
            ascending_num = ascending_order_number(num)
            print("Number in ascending order:", ascending_num)

            # Sort the digits included in the number
            sorted_digits_num = sort_digits_included(num)
            print("Sorted digits in the number:", sorted_digits_num)
        else:
            print("Invalid input! Please enter a four-digit natural number.")
    except ValueError:
        print("Invalid input! Please enter a valid four-digit natural number.")

if __name__ == "__main__":
    main()