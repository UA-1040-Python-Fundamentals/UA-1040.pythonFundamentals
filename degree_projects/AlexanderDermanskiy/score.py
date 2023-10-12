class Score:
    def __init__(self):
        self.score = 0

# Increase the player's score by a specified number of points (default: 1)
    def increase_score(self, points=1):
        self.score += points

# Get the current player's score
    def get_score(self):
        return self.score