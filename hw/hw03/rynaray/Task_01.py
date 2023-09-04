text = "'better', 'never' and 'is' in the given line."
word_better = "better"
word_never = "never"
word_is = "is"

count_occurrences = text.count(word_better)
count_occurrences = text.count(word_never)
count_occurrences = text.count(word_is)
print(f"number of words '{word_better}' in the text: {count_occurrences}")
print(f"number of words '{word_never}' in the text: {count_occurrences}")
print(f"number of words '{word_is}' in the text: {count_occurrences}")

text_in_uppercase = text.upper()
print(text_in_uppercase)

old_char = "i"
new_char = "&"

new_text = text.replace(old_char, new_char)
print(new_text)