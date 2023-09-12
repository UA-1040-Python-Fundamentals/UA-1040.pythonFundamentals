def count_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


input_str = input("Enter a string: ")
print("Number of characters:", count_char(input_str))