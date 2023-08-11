def interchange_values(a, b):
    print("Before interchange:")
    print("a =", a)
    print("b =", b)

    # Interchange the values without using a third variable
    a = a + b
    b = a - b
    a = a - b

    print("\nAfter interchange:")
    print("a =", a)
    print("b =", b)

# Example usage:
if __name__ == "__main__":
    num1 = 10
    num2 = 20
    interchange_values(num1, num2)