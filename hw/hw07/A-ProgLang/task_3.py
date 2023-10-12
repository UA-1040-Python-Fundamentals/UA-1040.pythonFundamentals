#Write a function that calculates the number of characters included in a given string
#• input: "hello"
#• output: {"h":1, "e":1,"l":2,"o":1}

def count_characters(input_string):
    character_count = {}
    for char in input_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

input_string = input("Enter a string: ")
result = count_characters(input_string)
print(result)