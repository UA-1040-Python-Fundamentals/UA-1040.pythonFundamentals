# Task 3. Write a function that calculates the number of characters included in a given string
# input: "Hello"
# output: {"h":1, "e":1, "l":2, "o":1}
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage:
input_string = "hello"
result = count_characters(input_string)
print(result)