def filter_words(line):
    line = line.lower()+' '+' '
    finalLine = ""
    for i in range(len(line)-1):
        if line[i] == ' ' and line[i+1] == ' ':
            pass
        else:
            finalLine += line[i]

    finalLine = finalLine.capitalize()
    return finalLine


print(filter_words("WOW this is REALLY          amazing"))
