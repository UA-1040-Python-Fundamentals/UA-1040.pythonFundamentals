# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

n = 1324
number_list = list(map(int, str(n)))

# Product
product = int(number_list[0]*number_list[1]*number_list[2]*number_list[3])
print("The product of the digits =", product)

# reverse_order = sorted(number_list, reverse=True)
# sorted_list = sorted(number_list)
# print(reverse_order)
# print(sorted_list)

# reverse = number_list[::-1]
# print(reverse)

number_list.reverse()
print("reverse order -", *number_list)

number_list.sort()
print("ascending order -", *number_list)

number_list.reverse()
print("descending order -", *number_list)

