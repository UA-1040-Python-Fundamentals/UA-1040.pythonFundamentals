import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "purple", "red", "yellow", "black"])


ghost = Ghost()
print(ghost.color)
