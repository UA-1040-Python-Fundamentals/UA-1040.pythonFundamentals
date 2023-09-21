def f(word):
    d = {}
    word = word.lower()
    for i in word:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    return d
print(f("heLlo"))
