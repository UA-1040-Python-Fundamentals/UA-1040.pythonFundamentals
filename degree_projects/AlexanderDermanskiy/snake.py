class Snake:
    def __init__(self, initial_x, initial_y):
        self.body = [(initial_x, initial_y)]  # Snake's body represented as a list of (x, y) coordinates
        self.direction = "RIGHT"  # Initial direction (you can choose any direction)
        self._should_grow = False  # Whether the snake should grow after eating food

    def move(self):
        # Calculate the new head position based on the current direction
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 10)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 10)
        elif self.direction == "LEFT":
            new_head = (head_x - 10, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 10, head_y)

        # Insert the new head at the front of the body
        self.body.insert(0, new_head)

        # Check if the snake should grow (eaten food)
        if not self._should_grow:
            self.body.pop()  # Remove the tail (last element) if not growing
        else:
            self._should_grow = False  # Reset the flag after growing

    def change_direction(self, new_direction):
        # Update the snake's direction, but prevent reversing
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction
    
    def get_body(self):
        # Return the entire snake's body
        return self.body
    
    def get_head_position(self):
        # Return the position of the snake's head
        return self.body[0]

    def check_collision(self, width, height):
        head_x, head_y = self.body[0]

        # Check if the snake collides with the walls
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True

        # Check if the snake collides with itself
        if len(self.body) > 1 and (head_x, head_y) in self.body[1:]:
            return True

        return False
    def grow(self):
        # Add a new segment to the snake's body (when it eats food)
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    
    # Add a method to check if the snake should grow
    def should_grow(self):
        return self._should_grow
    
    # Add a method to set whether the snake should grow
    def set_should_grow(self, value):
        self._should_grow = value