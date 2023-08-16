def characters_num(word):
    word_low = word.lower()
    dct = {}
    for i in word_low:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct

print(characters_num("hello"))
