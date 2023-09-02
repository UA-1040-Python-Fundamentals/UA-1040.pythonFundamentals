def filter_words(input_str):
    text = " ".join((input_str.capitalize()).split())
    return text

print(filter_words("THAT was EXTRAORDINARY!"))
print(filter_words("HELLO CAN YOU HEAR ME?"))