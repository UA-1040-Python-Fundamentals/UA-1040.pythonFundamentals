import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Test
if __name__ == "__main__":
    ghost = Ghost()
    print(f"The ghost's color is: {ghost.color}")

