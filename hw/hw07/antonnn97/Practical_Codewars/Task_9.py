def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


name1 = "Roman"
name2 = "Anton"
print(are_you_playing_banjo(name1))
print(are_you_playing_banjo(name2))