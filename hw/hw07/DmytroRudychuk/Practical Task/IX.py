# DESCRIPTION:
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

def to_play(word) -> str:
    """
    Answers the question "Do you play the banjo?".
    If your name starts with an "R" or a lowercase "r," you play the banjo
    """

    return word + " plays banjo" if word[0].upper() == "R" else word + " does not play banjo"

print(to_play("Roman"))
print(to_play("roman"))
print(to_play("Ivan"))