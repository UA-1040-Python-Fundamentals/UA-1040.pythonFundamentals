def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Test examples
print(reverse_words("Hello World"))
print(reverse_words("Hi There."))