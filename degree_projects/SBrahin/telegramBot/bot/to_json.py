import json

ar = []

with open('censor.txt', encoding='utf-8') as file:
    for i in file:
        word = i.lower().split('\n')[0]
        if word != '':
            ar.append(word)

with open('censor.json', 'w', encoding='utf-8') as el:
    json.dump(ar,el)
