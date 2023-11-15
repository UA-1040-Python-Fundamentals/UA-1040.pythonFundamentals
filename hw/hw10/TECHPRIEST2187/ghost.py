import random


class Ghost:
    def __init__(self, color=""):
        self.color = color


ghost = Ghost()

num = random.randint(1, 3)

if num == 1:
    ghost.color = "yellow"
elif num == 2:
    ghost.color = "purple"
else:
    ghost.color = "red"

print(ghost.color)



