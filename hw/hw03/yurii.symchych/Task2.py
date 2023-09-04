number = int(input("Enter a four-digit natural number: "))

product = (number // 1000) * ((number // 100) % 10) * ((number // 10) % 10) * (number % 10)
print("Product of digits:", product)

reverse_number = int(str(number)[::-1])
print("Number in reverse order:", reverse_number)

sorted_number = int("".join(sorted(str(number))))
print("Number with digits sorted in ascending order:", sorted_number)
