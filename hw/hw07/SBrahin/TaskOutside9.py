#Are You Playing Banjo?

def are_you_playing_banjo(name):
    # Implement me!
    if name.lower().startswith("r"):
        return name + " plays banjo"
    else:
         return name + " does not play banjo"

print(are_you_playing_banjo("Frenk"))
