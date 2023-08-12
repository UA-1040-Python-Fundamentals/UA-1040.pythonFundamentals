def word_to_dict(word) -> dict:
    """
    The function receives a string value and returns a dictionary with keys in the role of characters from the string and keys in the form of the number of the given character in the line
    """
    result = {}
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    print(result)
    return result

word = "The function receives a string value and returns a dictionary with keys in the role of characters from the string and keys in the form of the number of the given character in the line"

word_to_dict("hello")

