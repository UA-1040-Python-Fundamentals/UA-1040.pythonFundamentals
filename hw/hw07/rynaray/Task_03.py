def count_characters(input_string):
    count = {}
    for char in input_string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

input_str = (input("Enter your word: "))
print(count_characters(input_str))
