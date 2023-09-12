def filter_words(s):
    words = s.lower().split()
    words[0] = words[0].capitalize()
    return ' '.join(words)

# Test examples
print(filter_words('HELLO CAN YOU HEAR ME'))
print(filter_words('now THIS is REALLY interesting'))
print(filter_words('THAT was EXTRAORDINARY!'))
