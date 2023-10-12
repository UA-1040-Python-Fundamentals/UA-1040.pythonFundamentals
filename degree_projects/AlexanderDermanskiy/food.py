import random

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.randomize_position()

    # Generate a random position for the food within the game area
    def randomize_position(self):
        # Make sure it aligns with the grid (assuming each grid cell is 10x10 pixels)
        x = random.randrange(0, self.width, 10)  
        y = random.randrange(0, self.height, 10)
        return (x, y)

    def get_position(self):
        return self.position

    # Generate a new random position for the food when eaten by the snake
    def respawn(self):
        self.position = self.randomize_position()