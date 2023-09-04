# DESCRIPTION:
# Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(input_str) -> str:
    """
    The function takes a string and returns a formatted string where the first character of the first word is uppercase and all others are lowercase.
    """

    words = input_str.split()
    formatted_words = []

    for word in words:
        if word:
            formatted_word = word[0].upper() + word[1:].lower()
            if len(formatted_words) == 0:
                formatted_words.append(formatted_word)
            else:
                formatted_words.append(word.lower())

    formatted_string = " ".join(formatted_words)
    return formatted_string


print(filter_words('HELLO CAN YOU HEAR ME')) #=> Hello can you hear me
print(filter_words('now THIS is REALLY interesting')) #=> Now this is really interesting
print(filter_words('THAT was EXTRAORDINARY!')) #=> That was extraordinary!