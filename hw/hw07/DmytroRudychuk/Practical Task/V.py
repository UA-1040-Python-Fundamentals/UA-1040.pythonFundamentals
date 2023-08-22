# DESCRIPTION:
# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def revers_word(line) -> str:
    """
    Reversal of words in a line
    """
    res = list(line.split(" "))
    return " ".join(res[::-1])

print(revers_word("Hello World"))
print(revers_word("Hi There."))