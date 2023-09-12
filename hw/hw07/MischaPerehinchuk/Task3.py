def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_str = "Hello"
character_counts = count_characters(input_str)
print(character_counts)

